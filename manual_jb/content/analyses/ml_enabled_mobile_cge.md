# Machine Learning Enabled Computable General Equilibrium (CGE) - Mobile

**Description**

The "Machine Learning Enabled Computable General Equilibrium (CGE) - Mobile" analysis merges advanced machine learning with traditional CGE models to offer unprecedented insights into the economic impacts of disaster scenarios on Mobile. Trained on a comprehensive dataset of numerous simulated disasters and their economic effects, this hybrid approach excels in predicting the intricate dynamics of the city's economy under various crises.

A computable general equilibrium (CGE) model is based on fundamental economic principles. A CGE model uses multiple data sources to reflect the interactions of households, firms, and relevant government entities as they contribute to economic activity. The model is based on (1) utility-maximizing households that supply labor and capital, using the proceeds to pay for goods and services (both locally produced and imported) and taxes; (2) the production sector, with perfectly competitive, profit-maximizing firms using intermediate inputs, capital, land, and labor to produce goods and services for both domestic consumption and export; (3) the government sector that collects taxes and uses tax revenues in order to finance the provision of public services; and (4) the rest of the world.

The output of this analysis are CSV files with domestic supply, gross income, before- and post-disaster factor demand and household count.

**Contributors**

- Science: Charles Nicholson, Nushra Zannat, Hwayoung Jeon, Tao Lu, Harvey Cutler, Anita Pena
- Implementation: NCSA IN-CORE Dev Team


**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` | `str` | Output File Name prefix | Sets the file name prefix for output files.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`sector_shocks` <sup>*</sup> | [`incore:capitalShocks`](https://tools.in-core.org/semantics/api/types/incore:capitalShocks) | Capital shocks | Building states to capital <br>shocks per sector.

**Output datasets**

key name | type | name | description
--- | --- | --- | ---
`domestic-supply` <sup>*</sup> | [`incore:Employment`](https://tools.in-core.org/semantics/api/types/incore:Employment) | Supply results | A dataset containing domestic supply results (format: CSV).
`gross-income` <sup>*</sup> | [`incore:Employment`](https://tools.in-core.org/semantics/api/types/incore:Employment) | Gross income | A dataset of resulting gross income (format: CSV).
`pre-disaster-factor-demand` <sup>*</sup> | [`incore:FactorDemand`](https://tools.in-core.org/semantics/api/types/incore:FactorDemand) | Factor demand | A dataset of factor demand before disaster (format: CSV).
`post-disaster-factor-demand` <sup>*</sup> | [`incore:FactorDemand`](https://tools.in-core.org/semantics/api/types/incore:FactorDemand) | Factor demand | A dataset of factor demand after disaster (format: CSV).
`household-count` <sup>*</sup> | [`incore:HouseholdCount`](https://tools.in-core.org/semantics/api/types/incore:HouseholdCount) | Household count | A dataset of household count (format: CSV).

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create Machine Learning Enabled CGE Mobile Model
    mlcgemobile = MlEnabledCgeMobile(client)
    sector_shocks = "684345c99af67e7662654b36"
    mlcgemobile.load_remote_input_dataset("sector_shocks", sector_shocks)
    # optional
    mlcgemobile.set_parameter("result_name", "test_mobile_mlcge_result")
    mlcgemobile.run_analysis()
```

full analysis: [ml_enabled_mobile_cge.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/ml_enabled_mobile_cge.ipynb)