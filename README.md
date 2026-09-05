# Les Fourmis Du Web

Ce dépôt contient uniquement les données et la configuration du blog :

- `content/` : articles Markdown
- `config.yaml` : configuration du blog
- `.github/workflows/` : build et déploiement GitHub Pages
- `generator/` : submodule Git contenant le moteur de génération


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
style: "generator/assets/style8.css"
```

ou absolu :

```yaml
style: "/chemin/complet/vers/style.css"
```
