# Les Fourmis Du Web

Ce dépôt contient uniquement les données et la configuration du blog :

- `content/` : articles Markdown
- `config.yaml` : configuration du blog
- `.github/workflows/` : build et déploiement GitHub Pages
- `generator/` : submodule Git contenant le moteur de génération

## Ajouter le générateur comme submodule

Créer/publier d'abord le dépôt du générateur, puis depuis ce dépôt :

```bash
git submodule add <URL_DU_DEPOT_GENERATEUR> generator
git commit -m "Add static blog generator submodule"
```

Pour cloner ensuite le blog avec son générateur :

```bash
git clone --recurse-submodules <URL_DU_BLOG>
```

Sur un clone déjà existant :

```bash
git submodule update --init --recursive
```

## Build local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r generator/requirements.txt
python generator/build.py build --config config.yaml
```

Résultat dans `dist/`.

## CSS

Le chemin du CSS est défini dans `config.yaml`. Il peut être relatif au YAML :

```yaml
style: "assets/style8.css"
```

ou absolu :

```yaml
style: "/chemin/complet/vers/style.css"
```
