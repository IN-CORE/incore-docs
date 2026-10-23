# 5. Docs and example notebooks

Docs source: [incore-docs](https://github.com/IN-CORE/incore-docs). Branch from `develop`.

## Add an analysis page and notebook

- Page: `manual_jb/content/analyses/<name>.md`. Copy an existing page (e.g. `mean_dmg.md`): description, input parameters, input/output datasets, code snippet, link to the full notebook.
- Notebook: `notebooks/<name>.ipynb`.
- List the page in `manual_jb/content/analyses.md`.

## Register it in the table of contents

Add the page to `manual_jb/content/_toc.yml` under `analyses`:

```yaml
- file: analyses/<name>
```

## Build

```bash
cd manual_jb
pip install -r requirements.txt
jupyter-book build content
```

Open `content/_build/html/index.html` and check your page and links.
