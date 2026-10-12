# 5. Other scenarios

(dev-guides-incubator)=
## Contribute to pyincore-incubator

For community analyses not (yet) in core pyincore.

```bash
git clone https://github.com/IN-CORE/pyincore-incubator.git && cd pyincore-incubator
conda env create -f environment.yml && conda activate pyincore_incubator
pip install -e .
```

1. Add `pyincore_incubator/analyses/<your_analysis>/` (subclass `BaseAnalysis`).
2. Add a test under `tests/pyincore_incubator/` and an example notebook.
3. PR to `develop`.

Docs: [pyIncore Incubator](../pyincore_incubator.md)

## Prepare input data (pyincore-data)

Census, NSI building inventories, demographic inputs.

```bash
conda install -c in-core pyincore-data
```

- Docs: [pyIncore data](../pyincore_data.md)
- API: https://tools.in-core.org/doc/pyincore_data/index.html
- NSI inventory: [Create Building Inventory from NSI data](../notebooks/create_building_inventory_from_NSI/create_building_inventory_from_NSI.ipynb)

## Browse / inspect only (no code)

Web tools — Data, Hazard, DFR3 viewers: [IN-CORE Web Tools](../webtools.md)
DFR3 curve viewer: https://tools.in-core.org/DFR3Viewer

## Run notebooks with zero install

IN-CORE Lab (hosted JupyterLab, pyincore preinstalled): [IN-CORE Lab](../incore_lab.md)

## Call the REST API directly (non-Python clients)

- Swagger: https://tools.in-core.org/doc/api/
- Token: `POST https://tools.in-core.org/auth/realms/In-core/protocol/openid-connect/token` (client `react-auth`), then `Authorization: Bearer <token>`.

## Edit the docs (incore-docs)

```bash
git clone https://github.com/IN-CORE/incore-docs.git && cd incore-docs/manual_jb
conda create -n incore_docs -c conda-forge python=3.11 jupyter-book && conda activate incore_docs
jupyter-book build content      # open content/_build/html/index.html
```

- Pages: `manual_jb/content/*.md`, TOC: `manual_jb/content/_toc.yml`
- New analysis page: add `content/analyses/<name>.md` + notebook, register in `_toc.yml`.

## Upgrade old pyincore code

Breaking changes between versions: [pyIncore Upgrade Guide](../pyincore_upgrade.md)

## Help

- FAQ: [Frequently asked questions](../faq.md)
- Contact: [Contact Information](../contact.md)
- incore-dev@lists.illinois.edu · Slack https://in-core.slack.com/
