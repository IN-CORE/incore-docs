# Equity Metric

**Description**

The algorithm computes equity metrics to characterize the inequity present in the infrastructure service provision
between two groups of concerns’ (e.g., low income vs. non-low income, minority vs non-minority, etc.). The metrics are
built upon Theil’s T, which is a common metric to compute the inequality present in the dispersion of a scarce
resource (e.g., income). The metrics could also be implemented to assess inequity in different scenarios with other
scarce resources of concern.

To compute the metrics, a scarce resource should be formulated and calculated for an infrastructure application. The
scarce resource for infrastructure can be taken as any user defined relevant values, such as a resilience score (i.e.,
probability of service provision) or recovery time. We've included a companion utility class where we define and
prepare recovery time as a scarce resource. Other scarce resources can and could be explored if provided by the user.

The equity metric allows for an equity assessment of the current infrastructure service provision. It also enables the
assessment of equity gains for a given retrofit plan and can be integrated into an overall decision-making process..
The output metrics tell the following information 1) Theil's T - overall amount of inequality in scarce resource's
dispersion across a community (distributional inequity)  2) Between Zone Inequality (BZI) - amount of inequality
attributed to scarce resource differences between groups (restorative inequity), and 3) Within Zone Inequality (WZI) -
amount of inequality due to resource differences among singular groups.

**Contributors**

- Science: Abigail L. Beck, Ph.D, Eun Jeong Cha, Ph.D, Walter Peacock, Ph.D
- Implementation: NCSA IN-CORE Dev Team

**Related publications**

- Beck, A.L., Cha, E.J. & Peacock, W.G. "Incorporation of Equity into Infrastructure Decision-Making: Development of an
  Equity Metric for Infrastructure Retrofitting," The 14th International Conference on Applications of Statistics and
  Probability in Civil Engineering (ICASP14), Dublin, Ireland, July, 2023. http://hdl.handle.net/2262/103309

**Input parameters**

 key name                                | type  | name                          | description                                                                                                                                                                          
-----------------------------------------|-------|-------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 `result_name` <sup>*</sup>              | `str` | Result name                   | Name of the result dataset.                                                                                                                                                          
 `division_decision_column` <sup>*</sup> | `str` | Division decision column name | Column name of a binary variable associated with each household used to group it into two groups (e.g. low income vs non low income, minority vs non-minority, social vulnerability) 

**Input datasets**

 key name                               | type                                                                                                                | name               | description                                                            
----------------------------------------|---------------------------------------------------------------------------------------------------------------------|--------------------|------------------------------------------------------------------------
 `housing_unit_allocation` <sup>*</sup> | [`incore:housingUnitAllocation`](https://tools.in-core.org/semantics/api/types/incore:housingUnitAllocation) | Housing allocation | A housing unit allocation dataset.
 `scarce_resource` <sup>*</sup>         | [`incore:scarceResource`](https://tools.in-core.org/semantics/api/types/incore:scarceResource)               | Scarce resource    | Scarce resource dataset e.g. probability of service, return time, etc.

**Output datasets**

 key name                     | type                                                                                              | parent key | name          | description                                                                                           
------------------------------|---------------------------------------------------------------------------------------------------|------------|---------------|-------------------------------------------------------------------------------------------------------
 `equity_metric` <sup>*</sup> | [`incore:equityMetric`](https://tools.in-core.org/semantics/api/types/incore:equityMetric) |            | Equity Metric | CSV file of equity metric, including Theil’s T Value, Between Zone Inequality, Within Zone Inequality

<small>(* required)</small>

**Execution**

code snippet:

```
    client = IncoreClient()
    datasvc = DataService(client)

    # Example of preparing scarce resource
    repair_time_df = Dataset.from_data_service(housing_recovery_id, datasvc).get_dataframe_from_csv()
    scarce_resource_df = EquityMetricUtil.prepare_return_time_as_scarce_resource(
        repair_time_df
    )
    scarce_resource = Dataset.from_dataframe(
        scarce_resource_df, "scarce_resource", data_type="incore:scarceResource"
    )
    
    # Example of running equity metric analysis
    equity_metric = EquityMetric(client)
    equity_metric.set_parameter("result_name", "Galveston_recovery_time")
    equity_metric.set_parameter("division_decision_column", "SVI")
    equity_metric.load_remote_input_dataset(
        "housing_unit_allocation", housing_unit_allocation_id
    )
    equity_metric.set_input_dataset("scarce_resource", scarce_resource)
    equity_metric.run_analysis()
```

full analysis: [equity_metric.ipynb](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/equity_metric.ipynb)
