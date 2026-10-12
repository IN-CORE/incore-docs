# 1. Scientist: build a notebook from existing analyses and data

No code changes to pyincore. You chain existing analyses with existing (or your own) data.

## Where to run

| Option | Setup | Link |
|--------|-------|------|
| IN-CORE Lab (hosted, nothing to install) | Log in | [IN-CORE Lab](../incore_lab.md) |
| Local Jupyter | conda + pyincore | [Installation](../pyincore/install_pyincore.md) |

Local:

```bash
conda create -n incore -c conda-forge python=3.11
conda activate incore
conda install -c in-core pyincore pyincore-viz jupyter
jupyter lab
```

## Steps

1. Pick analyses → [Analyses](../analyses.md) (each page lists inputs, outputs, example notebook)
2. Find IDs for hazards / inventories / mappings → Web tools [IN-CORE Web Tools](../webtools.md)
3. Start from the closest testbed notebook and swap inputs.
4. Chain: pass one analysis's output to the next.

```python
bldg_dmg.run_analysis()
damage = bldg_dmg.get_output_dataset("ds_result")
func.set_input_dataset("building_damage", damage)
```

5. Visualize with pyincore-viz → [pyIncore viz](../pyincore_viz.md)

## Start from a testbed notebook

| Testbed | Notebook |
|---------|----------|
| Galveston, TX (hurricane) | [Galveston Testbed](../notebooks/Galveston_testbed/Galveston_testbed.ipynb) |
| Joplin, MO (tornado) | [Joplin_testbed.ipynb](../notebooks/Joplin_testbed/Joplin_testbed.ipynb) |
| Lumberton, NC (flood) | [Lumberton Testbed](../notebooks/Lumberton_testbed/Lumberton_testbed.ipynb) |
| Seaside, OR (EQ/tsunami) | [Seaside_testbed.ipynb](../notebooks/Seaside_testbed/Seaside_testbed.ipynb) |
| Mobile, AL | [Mobile Testbed](../notebooks/Mobile_testbed/Mobile_testbed.ipynb) |
| Memphis / MMSA (EQ, interdependent) | [Example Notebooks](../notebooks.md) |
| All notebooks | [Example Notebooks](../notebooks.md) |
| Raw `.ipynb` files | https://github.com/IN-CORE/incore-docs/tree/main/notebooks |

## Mixing in your own data

Same as {ref}`Algorithms § 2b <dev-guides-local-data>`: load local files with `Dataset.from_file`, `Earthquake.from_json_file`, `MappingSet.from_json_file` and pass them in place of remote IDs.

- Build an inventory from NSI: [Create Building Inventory from NSI data](../notebooks/create_building_inventory_from_NSI/create_building_inventory_from_NSI.ipynb)
- Census / demographic inputs: [pyIncore data](../pyincore_data.md)

## Learning path

Workshop (2023-11) — Jupyter intro → hazards → damage/recovery → local data:
[INSPIRE workshop November 15, 2023](../workshops/20231115/agenda.md)

## Next step

Need logic no existing analysis provides? → [Algorithms](algorithm.md)
