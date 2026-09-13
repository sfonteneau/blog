# Les Fourmis Du Web

This repository contains only the blog data and configuration:

- `content/`: Markdown articles
- `config.yaml`: blog configuration
- `.github/workflows/`: GitHub Pages build and deployment
- `generator/`: Git submodule containing the generation engine

## Local build

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r generator/requirements.txt
python generator/build.py build --config config.yaml
```

Output is generated in `dist/`.

## CSS

The CSS path is defined in `config.yaml`. It can be relative to the YAML file:

```yaml
style: "generator/assets/style8.css"
```

or absolute:

```yaml
style: "/full/path/to/style.css"
```