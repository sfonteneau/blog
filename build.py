#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Générateur de blog statique depuis Markdown (multi-langues FR/EN).

Entrée:
  content/posts/<key>/fr.md
  content/posts/<key>/en.md   (optionnel)
  content/posts/<key>/images/...   (images locales référencées comme images/...)

Front matter YAML requis:
  title: "..."        (obligatoire)
  date: "YYYY-MM-DD"  (obligatoire)
  slug: "..."         (obligatoire, par langue)
  lang: "fr"|"en"     (obligatoire)
  key:  "..."         (obligatoire; regroupe les traductions)

Templates / assets (fichiers à côté du script):
  templates/base.html
  templates/index.html
  templates/post.html
  assets/style.css
  assets/theme.js

Sortie:
  dist/index.html
  dist/<slug>/index.html
  dist/en/index.html
  dist/en/<slug>/index.html
  dist/assets/style.css
  dist/assets/theme.js
  dist/assets/img/<fichier.fingerprint.ext>

Commande:
  python build.py build
"""

from __future__ import annotations

import hashlib
import re
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime, date
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import unquote

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
import markdown as md


ROOT = Path(__file__).resolve().parent
POSTS_DIR = ROOT / "content" / "posts"
DIST_DIR = ROOT / "dist"
ASSETS_DIR = DIST_DIR / "assets"
CONFIG_FILE = ROOT / "config.yaml"

TEMPLATES_DIR = ROOT / "templates"
ASSETS_SRC_DIR = ROOT / "assets"


@dataclass
class Lang:
    code: str
    label: str
    path: str


@dataclass
class Post:
    key: str
    lang: str
    title: str
    slug: str
    date: date
    html: str
    excerpt: str
    translations: List[dict]

    @property
    def date_iso(self) -> str:
        return self.date.isoformat()

    @property
    def date_human(self) -> str:
        return self.date.strftime("%d/%m/%Y")

    @property
    def reading_time(self) -> str:
        words = max(1, len(re.findall(r"\w+", self.html)))
        minutes = max(1, int(round(words / 200)))
        return f"{minutes} min" if self.lang == "en" else f"{minutes} min de lecture"


FRONT_MATTER_RE = re.compile(r"^\s*---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)
IMG_MD_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
IMG_HTML_RE = re.compile(r'(<img\b[^>]*\bsrc=["\'])([^"\']+)(["\'])', re.IGNORECASE)


def ensure_clean_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def parse_front_matter(markdown_text: str, path: Path) -> Tuple[Dict[str, Any], str]:
    m = FRONT_MATTER_RE.match(markdown_text)
    if not m:
        raise ValueError(f"{path}: front matter YAML manquant.")
    fm_raw, body = m.group(1), m.group(2)
    fm = yaml.safe_load(fm_raw) or {}
    if not isinstance(fm, dict):
        raise ValueError(f"{path}: front matter invalide.")
    return fm, body


def parse_date(value: Any, path: Path) -> date:
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, str):
        return datetime.strptime(value.strip(), "%Y-%m-%d").date()
    raise ValueError(f"{path}: date invalide.")


def make_excerpt(html: str, max_chars: int = 180) -> str:
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= max_chars else (text[: max_chars - 1].rstrip() + "…")


def is_external(url: str) -> bool:
    u = url.lower().strip()
    return u.startswith("http://") or u.startswith("https://") or u.startswith("data:") or u.startswith("mailto:")


def clean_url(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("<") and raw.endswith(">"):
        raw = raw[1:-1].strip()
    parts = raw.split()
    return unquote(parts[0])


def fingerprint_copy(src: Path, dst_dir: Path) -> str:
    content = src.read_bytes()
    h = hashlib.sha256(content).hexdigest()[:10]
    dst_dir.mkdir(parents=True, exist_ok=True)
    out_name = f"{src.stem}.{h}{src.suffix.lower()}"
    out_path = dst_dir / out_name
    if not out_path.exists():
        out_path.write_bytes(content)
    return out_name


def process_images_in_text(body: str, md_path: Path, rel_from_post: str) -> str:
    """
    Copie les images référencées en local (images/...) vers dist/assets/img avec fingerprint,
    puis réécrit les URLs dans le markdown (ou HTML inline) pour pointer vers ../../assets/img/.. selon profondeur.
    """
    out_img_dir = ASSETS_DIR / "img"

    def copy_and_rewrite(url: str) -> Optional[str]:
        url = clean_url(url)
        if is_external(url) or url.startswith("/"):
            return None
        src = (md_path.parent / url).resolve()
        if not src.exists() or not src.is_file():
            return None
        out_name = fingerprint_copy(src, out_img_dir)
        return f"{rel_from_post}/assets/img/{out_name}"

    def md_repl(m: re.Match) -> str:
        alt, raw = m.group(1), m.group(2)
        new_url = copy_and_rewrite(raw)
        return m.group(0) if not new_url else f"![{alt}]({new_url})"

    body = IMG_MD_RE.sub(md_repl, body)

    def html_repl(m: re.Match) -> str:
        prefix, src, suffix = m.group(1), m.group(2), m.group(3)
        new_url = copy_and_rewrite(src)
        return m.group(0) if not new_url else f"{prefix}{new_url}{suffix}"

    body = IMG_HTML_RE.sub(html_repl, body)
    return body


def load_config() -> Tuple[Dict[str, Any], List[Lang]]:
    data = yaml.safe_load(read_text(CONFIG_FILE)) if CONFIG_FILE.exists() else {}
    data = data or {}
    data.setdefault("site", {})
    data.setdefault("menu", [])
    data.setdefault("languages", [{"code": "fr", "label": "FR", "path": "/"}, {"code": "en", "label": "EN", "path": "/en/"}])
    site = data["site"]
    site.setdefault("title", "Mon Blog")
    site.setdefault("tagline", "")
    site.setdefault("author", "")
    langs = [Lang(code=l["code"], label=l.get("label", l["code"].upper()), path=l.get("path", f"/{l['code']}/")) for l in data["languages"]]
    return data, langs


def iter_markdown_files() -> List[Path]:
    return sorted([p for p in POSTS_DIR.rglob("*.md") if p.is_file()]) if POSTS_DIR.exists() else []


def compute_rel(depth: int) -> str:
    return "." if depth == 0 else "/".join([".."] * depth)


def copy_static_assets() -> None:
    # Copy assets/style.css + assets/theme.js -> dist/assets/
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    for name in ("style.css", "theme.js"):
        src = ASSETS_SRC_DIR / name
        if not src.exists():
            raise FileNotFoundError(f"Fichier asset manquant: {src}")
        shutil.copy2(src, ASSETS_DIR / name)


def build() -> None:
    cfg, languages = load_config()
    menu = cfg.get("menu", [])
    site = cfg["site"]

    ensure_clean_dir(DIST_DIR)
    copy_static_assets()

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    now_year = datetime.now().year

    raw_posts = []
    for md_path in iter_markdown_files():
        fm, body = parse_front_matter(read_text(md_path), md_path)
        title = str(fm.get("title", "")).strip()
        slug = str(fm.get("slug", "")).strip()
        lang = str(fm.get("lang", "")).strip()
        key = str(fm.get("key", "")).strip()
        if not (title and slug and lang and key and fm.get("date")):
            raise ValueError(f"{md_path}: champs requis manquants (title, date, slug, lang, key).")
        d = parse_date(fm.get("date"), md_path)
        raw_posts.append({"path": md_path, "title": title, "slug": slug, "lang": lang, "key": key, "date": d, "body": body})

    # group by key -> lang -> post
    by_key: Dict[str, Dict[str, dict]] = {}
    for rp in raw_posts:
        by_key.setdefault(rp["key"], {})[rp["lang"]] = rp

    posts: List[Post] = []
    for key, langs_map in by_key.items():
        for lang_code, rp in langs_map.items():
            translations = []
            if lang_code == "fr" and "en" in langs_map:
                translations.append({"label": "EN", "url": f"../en/{langs_map['en']['slug']}/"})
            if lang_code == "en" and "fr" in langs_map:
                translations.append({"label": "FR", "url": f"../../{langs_map['fr']['slug']}/"})

            depth = 1 if lang_code == "fr" else 2
            rel_from_post = compute_rel(depth)
            processed = process_images_in_text(rp["body"], rp["path"], rel_from_post)
            html = md.markdown(processed, extensions=["fenced_code", "tables", "toc"], output_format="html5")
            excerpt = make_excerpt(html)
            posts.append(Post(key=key, lang=lang_code, title=rp["title"], slug=rp["slug"], date=rp["date"], html=html, excerpt=excerpt, translations=translations))

    posts_by_lang: Dict[str, List[Post]] = {}
    for p in posts:
        posts_by_lang.setdefault(p.lang, []).append(p)
    for lc in posts_by_lang:
        posts_by_lang[lc].sort(key=lambda x: x.date, reverse=True)

    # Render indexes
    for lang in languages:
        lc = lang.code
        lang_posts = posts_by_lang.get(lc, [])
        if lc == "fr":
            out_dir = DIST_DIR
            rel = "."
            home_href = "./index.html"
        else:
            out_dir = DIST_DIR / lc
            out_dir.mkdir(parents=True, exist_ok=True)
            rel = ".."
            home_href = "./index.html"

        view_posts = []
        for p in lang_posts:
            view_posts.append({
                "title": p.title,
                "date_iso": p.date_iso,
                "date_human": p.date_human,
                "reading_time": p.reading_time,
                "excerpt": p.excerpt,
                "url": f"./{p.slug}/",
            })

        index_html = env.get_template("index.html").render(
            page_title=site["title"],
            site=site,
            menu=menu,
            posts=view_posts,
            rel=rel,
            now_year=now_year,
            languages=[{"code": l.code, "label": l.label, "path": l.path} for l in languages],
            lang={"code": lang.code, "label": lang.label, "path": lang.path},
            home_href=home_href,
        )
        (out_dir / "index.html").write_text(index_html, encoding="utf-8")

    # Render posts
    for p in posts:
        if p.lang == "fr":
            out_dir = DIST_DIR / p.slug
            out_dir.mkdir(parents=True, exist_ok=True)
            rel = ".."
            home_href = "../index.html"
            lang_obj = {"code": "fr", "label": "FR", "path": "/"}
        else:
            out_dir = DIST_DIR / "en" / p.slug
            out_dir.mkdir(parents=True, exist_ok=True)
            rel = "../.."
            home_href = "../index.html"
            lang_obj = {"code": "en", "label": "EN", "path": "/en/"}

        post_html = env.get_template("post.html").render(
            page_title=f"{p.title} — {site['title']}",
            site=site,
            menu=menu,
            post={
                "title": p.title,
                "date_iso": p.date_iso,
                "date_human": p.date_human,
                "reading_time": p.reading_time,
                "html": p.html,
                "translations": p.translations,
            },
            rel=rel,
            now_year=now_year,
            languages=[{"code": l.code, "label": l.label, "path": l.path} for l in languages],
            lang=lang_obj,
            home_href=home_href,
        )
        (out_dir / "index.html").write_text(post_html, encoding="utf-8")

    print(f"✅ Build terminé: {DIST_DIR}")


def main(argv: List[str]) -> int:
    cmd = (argv[1] if len(argv) > 1 else "build").lower()
    if cmd == "build":
        build()
        return 0
    print("Usage: python build.py build")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
