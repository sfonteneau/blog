---
title: "J’ai migré mon blog WordPress vers un site statique en Markdown (avec un petit script Python)"
date: "2026-02-01"
slug: "migration-wordpress-vers-statique-markdown-python"
lang: "fr"
key: "migration-wordpress-statique-markdown-python"
---

![Schéma d’une migration de WordPress vers Markdown avec Python](images/wp_to_md.png)

Pendant longtemps, mon blog tournait sous **WordPress**. Ça marche très bien, mais je n’avais plus besoin de toute la “machine” : base de données, plugins, mises à jour, surface d’attaque, etc.

Je voulais quelque chose de :

- **simple à maintenir**
- **rapide à servir**
- **facile à versionner**
- **portable** (un dossier à copier, point)

Du coup j’ai fait une migration vers un **blog statique**, généré à partir de **fichiers Markdown**.

## Le principe

Chaque article est un fichier `.md` avec un front-matter YAML :

```yaml
---
title: "Mon titre"
date: "YYYY-MM-DD"
slug: "mon-slug"
lang: "fr"
key: "mon-identifiant"
---
```

Le contenu est en **Markdown** (avec images locales possibles).  
Et un **script Python** génère le site final en HTML :

- une page d’accueil avec la liste des articles (du plus récent au plus ancien)
- une page par article, directement à l’URL du **slug** (`/<slug>/`)
- support des traductions (ex: `fr.md` / `en.md`) quand elles existent
- un design simple, avec un bouton **dark/light mode**

## Pourquoi j’aime bien cette approche

- Plus de base de données
- Plus de backend à maintenir
- Déploiement “bête” : tu sers le dossier `dist/` et ça marche
- Tout est versionnable via Git (articles, assets, config, templates…)

## Le code est dispo

Si ça peut servir à d’autres, j’ai mis le script et la structure du projet sur mon GitHub.

👉 Tout est ici : [GitHub](https://github.com/sfonteneau/blog)


