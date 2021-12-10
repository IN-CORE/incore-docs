### Multi-objective retrofit optimization model

**Description**

This analysis computes a series of linear programming models for single- and multi-objective optimization related 
to the effect of extreme weather on a community in terms of three objective functions. The three objectives used 
in this program are to minimize **economic loss**, minimize **population dislocation**, and maximize **building functionality**. 

This analysis computes a series of linear programming models for single- and multi-objective optimization related 
to the effect of extreme weather on a community in terms of three objective functions. The three objectives used 
in this program are to minimize **economic loss**, minimize **population dislocation**, and maximize **building functionality**. 
The analysis uses the set of mitigation strategies, which is determined by the hazard type. For instance, seismic 
mitigation on existing buildings includes reinforcing buildings with cross bracing, reinforcing buildings using 
shear walls, install shear anchors, etc. For tsunami and flooding hazards, relocation is one of the mitigation 
strategies. Various parameters represent, for example, the starting and final retrofitting level of a building, 
the retrofitting cost for buildings retrofitted from one level to another in groups of structural types, 
or a coefficient of objective, which represents a community resilience goal to measure the performance of a system. 
The total number of objectives of the optimization model implemented in **pyIncore** is currently three; 
economic loss, population dislocation and building functionality constraints.

The computation proceeds by iteratively solving constrained linear models using epsilon steps. The CSV outputs 
of the computation are collections of optimal resource allocations.

**Contributors**

- Science: Charles Nicholson and Yunjie Wen
- Implementation: Dale Cochran, Tarun Adluri, Jorge Duarte, Diego Calderon, Santiago Núñez-Corrales, and NCSA IN-CORE Dev Team

**Related publications**

**Input parameters**

key name | type | name | description
--- | --- | --- | ---
`result_name` | `str` | Result name | Result CSV dataset name.
`model_solver` | `str` | Model solver | Choice of the model solver to use. Gurobi is the default solver.
`num_epsilon_steps` <sup>*</sup> | `int` | Epsilon values | Number of epsilon values to evaluate.
`max_budget` <sup>*</sup> | `str` | Maximum budget | Selection of maximum possible budget.
`budget_available` | `float` | Budget value | Custom budget value.
`inactive_submodels` | `[int]` | Identifier of submodels | Identifier of submodels to inactivate during analysis.
`scale_data` <sup>*</sup>  | `bool` | Scaling data | Choice for scaling data.
`scaling_factor` | `float` | Scaling factor | Custom scaling factor.

**Input datasets**

key name | type | name | description
--- | --- | --- | ---
`building_related_data` <sup>*</sup> | `incore:multiobjectiveBuildingRelatedData` | Building-related data |  A csv file with building-related data.
`strategy_costs_data` <sup>*</sup> | `incore:multiobjectiveStrategyCost` | Strategy cost | A csv file with strategy cost data per building.

**Output datasets**

key name | type | parent key | name | description
--- | --- | --- | --- | ---
`optimal_solution_dv_x` <sup>*</sup> | `incore:multiobjectiveOptimalSolutionX` |  | Results | A csv file with an optimal solution for decision variable x for Economic loss, Population dislocation and Building functionality values, results of objective function values.
`optimal_solution_dv_y` <sup>*</sup> | `incore:multiobjectiveOptimalSolutionY` |  | Results | A csv file with an optimal solution for decision variable y with initial and final retrofitted strategies for Economic loss, Population dislocation and Building functionality values, results of objective function values.

<small>(* required)</small>

**Execution**

code snippet:

```
    # Create Multi-objective retrofit optimization instance
    opt = `MultiObjectiveRetrofitOptimization`(client)

    # Load input dataset
    opt.load_remote_input_dataset("building_repairs_data", building_repairs_data)
    opt.load_remote_input_dataset("strategy_costs_data", strategy_costs_data)

    # Specify the result name
    result_name = "Multi_objective_retrofit_optimization"

    # Set analysis parameters
    opt.set_parameter("result_name", result_name)
    opt.set_parameter("model_solver", "Gurobi")
    opt.set_parameter("num_epsilon_steps", 10)
    opt.set_parameter("max_budget", max_budget)
    opt.set_parameter("budget_available", 1000000)
    opt.set_parameter("inactive_submodels", [inactive_submodels])
    opt.set_parameter("scale_data", True)
    opt.set_parameter("scaling_factor", 1.0)
    
    # Run Multi-objective retrofit optimization analysis
    opt.run_analysis()
```

full analysis: [multi_retrofit_optimization.ipynb](https://github.com/IN-CORE/incore-docs/blob/master/notebooks/multi_retrofit_optimization.ipynb) <br />
