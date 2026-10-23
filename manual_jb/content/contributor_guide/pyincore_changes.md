# 4. Fix bugs or change pyIncore / pyIncore-viz

## Editable install

See [Working with Python → Install from source](python_environment.md). Then install the pre-commit hooks:

```bash
pre-commit install
```

## Run tests

Tests use the dev services. Put the test credentials file at `tests/pyincore/.incorepw` first; ask for it via the channels in [Before you start](../contributor_guide.md). Never commit it.

```bash
python -m pytest --ignore=tests/test_format.py --ignore=tests/pyincore/analyses   # what CI runs
python tests/pyincore/analyses/<name>/test_<name>.py                                 # one analysis script
```

## Pre-commit (black, flake8)

Runs on every commit. To check everything:

```bash
pre-commit run --all-files
```

## Pull request

1. Branch from `develop`, named after the issue (e.g. `276-add-combined-building-loss`).
2. Update `CHANGELOG.md`.
3. Open a PR against `develop`.

More (dependency changes, CI details): [IN-CORE Developer Setup](https://github.com/IN-CORE/IN-CORE/wiki/IN%E2%80%90CORE-Developer-Setup) (wiki).
