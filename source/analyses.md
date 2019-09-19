## pyIncore analyses

### Bridge damage analysis

This analysis computes the damage to bridges based on a particular hazard such as earthquake, tsunami
and tornado by calling fragility and hazard services.

The process is similar to evaluating other structural damages. The probabilities for building damage
state are obtained using fragility curves and a hazard definition, each building site will have
a specific PGA (Peak Ground Acceleration), a measurement of an earthquake hazard for each scenario.
Liquefaction effect, which is defined as a change in stress condition, in which material that is ordinarily
a solid behaves like a liquid can be considered as well. The LMF (Liquefaction Modification Factor)
values are implemented as multiplication factors to the median fragility values and they must be present
in the dataset.

The code covers Normal and LogNormal fragilities with 4 limit states (slight, moderate, extensive
and complete) and creates an output CSV file.

**Required Parameters**

1. **Result name** A name for the result dataset, usually in CSV format which contains the damage information.
2. **Bridge Dataset ID** A bridge dataset you want to calculate damage for.
3. **Hazard Type** A hazard type for calculating bridge damage. E.g Earthquake
4. **Hazard ID** A hazard ID for calculating bridge damage.  Generally, hazards with PGA values are used to calculate bridge damages.
5. **Mapping ID** Default bridge fragility mapping on Incore-service. It implicitly defines the fragilities to be used in the calculation.
6. **Damage Ratios** A dataset that contains the damage ratios for bridges. It includes weights to compute mean damage.


**Optional Parameters**


1. **Liquefaction** Use liquefaction to modify fragility curve. Default False.
2. **Number of CPUs** Number of CPUs used for parallel computations. Default 1.


### Building damage analysis

This analysis computes the damage to buildings based on a particular hazard such as earthquake, tsunami
and tornado by calling fragility and hazard services.

The process is similar to evaluating other structural damages. The probabilities for building damage
state are obtained using fragility curves and a hazard definition, each building site will have
a specific PGA (Peak Ground Acceleration), a measurement of an earthquake hazard for each scenario.
Liquefaction effect, which is defined as a change in stress condition, in which material that is ordinarily
a solid behaves like a liquid can be considered as well. The LMF (Liquefaction Modification Factor)
values are implemented as multiplication factors to the median fragility values and they must be present
in the dataset.

The code covers Normal and LogNormal fragilities with 4 limit states (slight, moderate, extensive
and complete) and creates an output CSV file.

**Required Parameters**

1. **Result name** A name for the result dataset, usually in CSV format which contains the damage information.
2. **Building Dataset ID** A building dataset you want to calculate damage for.
3. **Hazard Type** A hazard type for calculating building damage. E.g Earthquake
4. **Hazard ID** A hazard ID for calculating building damage. Generally, hazards with PGA values are used to calculate building damages.
5. **Mapping ID** Default building fragility mapping on Incore-service. It implicitly defines the fragilities to be used in the calculation.
6. **Damage Ratios** A dataset that contains the damage ratios for buildings. It includes weights to compute mean damage.


**Optional Parameters**

1. **Liquefaction** Use liquefaction to modify fragility curve. Default False.
2. **Number of CPUs** Number of CPUs used for parallel computations. Default 1.


### Cummulative building damage analysis

This analysis computes the damage to buildings based on two hazards, an earthquake and a tsunami.

The process of evaluating structural damages is done externally and the results for earthquake and tsunami
are imported to the analysis. The damage intervals are then calculated from combined limit states.

**Required Parameters**

1. **Result name** A name for the result dataset, usually in CSV format which contains the damage information.
2. **Earthquake Building Damage** A building dataset with calculated damages caused by the earthquake.
2. **Tornado Building Damage** A building dataset with calculated damages caused by the tsunami.
3. **Damage Ratios** A dataset that contains the damage ratios for buildings. It includes weights to compute mean damage.

**Optional Parameters**

1. **Number of CPUs** Number of CPUs used for parallel computations. Default 1.


### Electric power network recovery model analysis

This analysis computes the damage to electric power network caused by hurricane hazard by calling fragility
and hazard services. It also deals with network recovery. The analysis is based on research of Vulnerability
and Robustness of Civil Infrastructure Systems to Hurricanes by Prof. Shuoqi Wang, Department of Civil and
Environmental Engineering, University of Washington.

The analysis calculates wind hazard, storm surge and rainfall levels within each zip code boundary. There are
multiple models based upon the three hazards of wind speed, storm surge inundation and rainfall.
The user has the option of making the selection of the fragility function.

The code creates an output CSV file.

**Required Parameters**

1. **Result name** A name for the result dataset, usually in CSV format which contains the damage information.
2. **Boundary ID** A parcel and zip code boundary shapefiles dataset you want to calculate damage for.
3. **Rain ID** A dataset (raster) of maximum daily total rainfall (in millimeters).
4. **Surge ID** A dataset (raster) representing an inland water inundation level above ground (in meters).
5. **Wind ID** A hurricane hazard dataset (raster) that contains the maximum sustained wind speeds (in meters per second).


**Related publications**

* Systems-Based Approach to Interdependent Electric Power Delivery and Telecommunications Infrastructure Resilience Subject to Weather-Related Hazards, D.A. Reed, S. Wang, K.C. Kapur and C. Zheng, *Journal of Structural Engineering* **142(8)** C4015011, 2015, doi: [10.1061/(ASCE)ST.1943-541X.0001395](https://opensource.ncsa.illinois.edu/confluence/display/INCORE2/Reed\_Wang\_Kapur\_Zheng2015.pdf)
* Vulnerability and Robustness of Civil Infrastructure Systems to Hurricanes, S. Wang, D.A. Reed, *Frontiers in Built Environment* **3** 60, 2017, doi: [10.3389/fbuil.2017.00060](https://opensource.ncsa.illinois.edu/confluence/display/INCORE2/Vulnerability\_and\_Robustness\_of\_Civil\_Infrastructu.pdf)


### Housing unit allocation analysis

This analysis sets up a detailed critical infrastructure inventory with housing unit level characteristics.
The process aligns the housing unit inventory with physical systems, such as the inventory of buildings
and the demand nodes of a potable water network. The allocation of housing units to the address points
(buildings) provides a framework to account for uncertainty in community structure that allows
for the hazard impacts to be analyzed statistically.

Additionally, the code can be used as a MCS analysis with n runs  or as a single allocation run with an integer
value being used as a random number generator seed and passed to the other analyses. Output is a tabulated
Housing Unit Allocation dataset.

**Required Parameters**

1. **Result name** A name for the result dataset, usually in CSV format which contains the damage information.
2. **Address Point Inventory ID** A dataset with the four probabilities of damage states from which the building value losses are calculated.
3. **Building Inventory ID** A building dataset with housing units.
4. **Critical Infrastructure Inventory ID** A dataset with water network inventory with corresponding infrastructure nodes.
5. **Housing Unit Inventory ID** A dataset with housing unit characteristics data based on 2010 Census.


**Optional Parameters**

1. **Seed** An integer value being imported to seed the random number generator.


**Related publications**

* Integration of Detailed Household Characteristic Data with Critical Infrastructure and Its Implementation to Post-Hazard Resilience Modeling, N. Rosenheim, R. Guidotti and P. Gardoni, [pdf](https://opensource.ncsa.illinois.edu/confluence/display/INCORE1/Stochastic+Population+Allocation?preview=/131104825/131104832/Rosenheim%20Integration%20of%20Detailed%20Household%20Characteristic%20Data%20with%20Critical%20Infrastructure%202018-06-07.pdf)
* Integration of Physical Infrastructure and Social Systems in Communities Reliability and Resilience Analysis, R. Guidotti, P. Gardoni and N. Rosenheim, *Reliability Engineering & System Safety*, 2019, doi: [10.1016/j.ress.2019.01.008](https://app.dimensions.ai/details/publication/pub.1111322263?and_facet_journal=jour.1158471)


### Joplin CGE Analysis

This analysis sets up an estimate of economic impact of Joplin tornado using Computable general equilibrium (CGE)
models. A detailed analysis shows how an economy might react to economic shocks, such as changes in policy, technology,
or natural disasters. A CGE model consists of equations describing model variables and a detailed database consistent
with the model equations.

The resulting datasets are 1) Domestic Supply, 2) employment and 3) household income.

**Required Parameters**

1. **Solver path** A system path to ipopt solver executable.
2. **Model iterations** A number of dynamic model iterations.
3. **SAM** Social accounting matrix.
4. **BB** Capital comp.
5. **IOUT** Government parameters and initial values.
6. **MISC** Parameters and initial values.
7. **MISCH** Household parameters and initial values.
8. **LANDCAP** Land capital.
9. **EMPLOY** Employment.
10. **IGTD** Exogenous Transfer PMT.
11. **TAUFF** Tax rates.
12. **TPC** Factor taxes.
13. **JOBCR** Labor.
14. **OUTCR** Commuter Labor Groups.


**Related publications**


### Nonstructural building damage analysis

This analysis computes the non-structural damage to buildings based on earthquake hazard by calling fragility and
hazard services.

The process is similar to evaluating other structural damages. The probabilities for building damage
state are obtained using fragility curves and a hazard definition, each building site will have
a specific PGA (Peak Ground Acceleration), a measurement of an earthquake hazard for each scenario.
Liquefaction effect, which is defined as a change in stress condition, in which material that is ordinarily
a solid behaves like a liquid can be considered as well. The LMF (Liquefaction Modification Factor)
values are implemented as multiplication factors to the median fragility values and they must be present
in the dataset.

The code covers Normal and LogNormal fragilities with 4 limit states (slight, moderate, extensive
and complete) and creates an output CSV file.

**Required Parameters**

1. **Result name** A name for the result dataset, usually in CSV format which contains the damage information.
2. **Building Dataset ID** A building dataset you want to calculate damage for.
3. **Hazard Type** A hazard type for calculating building damage. E.g Earthquake.
4. **Hazard ID** A hazard ID for calculating building damage. Generally, hazards with PGA values are used to calculate building damages.
5. **Mapping ID** Default building fragility mapping on Incore-service. It implicitly defines the fragilities to be used in the calculation.
6. **Acceleration-sensitive Damage Ratios** A dataset that contains the acceleration-sensitive (AS) damage ratios for buildings.
7. **Drift-sensitive Damage Ratios** A dataset that contains the drift-sensitive (DS) damage ratios for buildings.
8. **Content Damage Ratios** A dataset that contains the content damage ratios for buildings.


**Optional Parameters**

1. **Liquefaction** Use liquefaction to modify fragility curve. Default False. If True provide liquefaction geology dataset ID.
2. **Uncertainty** Use hazard uncertainty to modify fragility curve. Default False.
3. **Number of CPUs** Number of CPUs used for parallel computations. Default 1.


### Pipeline damage analysis

This analysis computes the damage to pipelines based on a particular hazard such as earthquake, tsunami
and tornado by calling fragility and hazard services.

The process is similar to evaluating other structural damages. The probabilities for pipeline damage
state are obtained using fragility curves and a hazard definition, each pipeline will have
a specific PGA (Peak Ground Acceleration), a measurement of an earthquake hazard for each scenario.
Liquefaction effect, which is defined as a change in stress condition, in which material that is ordinarily
a solid behaves like a liquid can be considered as well. The LMF (Liquefaction Modification Factor)
values are implemented as multiplication factors to the median fragility values and they must be present
in the dataset.

The code covers Normal and LogNormal fragilities with 4 limit states (slight, moderate, extensive
and complete) and creates an output CSV file.

**Required Parameters**

1. **Result name** A name for the result dataset, usually in CSV format which contains the damage information.
2. **Pipeline Dataset ID** A pipeline dataset you want to calculate damage for.
3. **Hazard Type** A hazard type for calculating pipeline damage. E.g Earthquake
4. **Hazard ID** A hazard ID for calculating pipeline damage.  Generally, hazards with PGA values are used to calculate pipeline damages.
5. **Mapping ID** Default pipeline fragility mapping on Incore-service. It implicitly defines the fragilities to be used in the calculation.
6. **Damage Ratios** A dataset that contains the damage ratios for pipelines. It includes weights to compute mean damage.


**Optional Parameters**

1. **Liquefaction** Use liquefaction to modify fragility curve. Default False.
2. **Number of CPUs** Number of CPUs used for parallel computations. Default 1.


### Population dislocation analysis

This analysis computes the population dislocation based on a particular hazard such as earthquake. First, Housing units, with detailed characteristics (tenure, household size, occupied, or vacant) are allocated to the address points (buildings). This is done by calling the Housing Unit Allocation analysis.

After the housing units are allocated, the hazard event defined by calling fragility and hazard services would determine the value loss for each structure which would be the input for the dislocation calculation. The dislocation is calculated from four probabilities of dislocation based on a random beta distribution of the four damage factors presented by Bai et al. 2009. These four damage factors correspond to value loss. The sum of the four probabilities multiplied by the four probabilities of damage states is used as the probability for dislocation. Since the process to determine which households are dislocated is probabilistic an integer value being imported to seed the random number generator determines if a household dislocates.

Additionally, the Block Group characteristics, percentages of African-American and Hispanic population are taken into account. The output is a CSV file with dislocated households and related variables.

**Required Parameters**

1. **Result name** A name for the result dataset, usually in CSV format which contains the damage information.
2. **Building Damage Dataset ID** A dataset with the four probabilities of damage states from which the building value losses are calculated.
3. **Housing Unit Allocation ID** A dataset with results of Housing Unit Allocation analysis.
4. **Block Group ID** A dataset ID with block group characteristics, percentages of African-American and Hispanic population.


**Optional Parameters**

1. **Seed** An integer value being imported to seed the random number generator.


**Related publications**

* Probabilistic Assessment of Structural Damage due to Earthquakes for Buildings in Mid-America, J. Bai; M.B.D. Hueste and P. Gardoni, *Journal of Structural Engineering* **135(10)** 2009, doi: [10.1061/(ASCE)0733-9445(2009)135%3A10(1155)](https://ascelibrary.org/doi/10.1061/%28ASCE%290733-9445%282009%29135%3A10%281155%29)
* Integration of Physical Infrastructure and Social Systems in Communities Reliability and Resilience Analysis, R. Guidotti, P. Gardoni and N. Rosenheim, *Reliability Engineering & System Safety*, 2019: DOI [10.1016/j.ress.2019.01.008](https://app.dimensions.ai/details/publication/pub.1111322263?and_facet_journal=jour.1158471)


### Tornado epn damage analysis

This analysis computes the damage to electric power network (EPN) caused by tornado hazard by calling fragility
and hazard services.  The probabilities for EPN damage state are obtained using network tower and network pole
fragility curves. Depending on the input data the analysis also provide information about the number of damaged
poles for each node, repair cost for each node, total repair cost for the network and total repair time for the network.

The code creates an output CSV file.

**Required Parameters**

1. **Result name** A name for the result dataset, usually in CSV format which contains the damage information.
2. **Tornado ID** A tornado ID for calculating power network damage. The tornado is defined by its shape file.
3. **Electric Power Network Node ID** A power nodes shapefile dataset you want to calculate damage for.
4. **Electric Power Network Link ID** A power network link shapefile dataset you want to calculate damage for.


### Transportation recovery analysis

This analysis computes the damage to bridges first calling the bridge damage analysis. It then uses nodes and
links in transportation path and Average daily traffic (ADT) data of bridges to calculate a Transportation
network post-disaster recovery.

Additionally, the analysis can be used in stochastic calculations with an integer value being imported to seed the random number generator.

The code creates an output CSV file with recovery trajectory timelines and data.

**Required Parameters**

1. **Result name** A name for the result dataset, usually in CSV format which contains the damage information.
2. **Bridge Dataset ID** A bridge dataset you want to calculate damage for.
3. **Hazard Type** A hazard type for calculating bridge damage. E.g Earthquake
4. **Hazard ID** A hazard ID for calculating bridge damage.  Generally, hazards with PGA values are used to calculate bridge damages.
5. **Mapping ID** Default bridge fragility mapping on Incore-service. It implicitly defines the fragilities to be used in the calculation.
6. **Damage Ratios** A dataset that contains the damage ratios for bridges. It includes weights to compute mean damage.
7. **Bridge Mapping ID** Default bridge fragility mapping on Incore-service. It implicitly defines the fragilities to be used in the calculation.
8. **Average Daily Traffic** An average daily trafic shapefile dataset.
9. **Transportation Node ID** A transportation (path) nodes shapefile dataset you want to calculate damage for.
10. **Transportation Link ID** A transportation (path) link shapefile dataset you want to calculate damage for.


**Optional Parameters**

1. **Bridge liquefaction** Use liquefaction to modify bridge fragility curve. Default False.
2. **Number of CPUs** Number of CPUs used for parallel computations. Default 1.


### Water facility damage analysis

This analysis computes the damage to water facilities, tanks, pumping stations etc. based on a particular hazard
such as earthquake, tsunami and tornado by calling fragility and hazard services.

The process is similar to evaluating other structural damages. The probabilities for water facilities damage
state are obtained using fragility curves and a hazard definition, each water facilities will have
a specific PGA (Peak Ground Acceleration), a measurement of an earthquake hazard.
Liquefaction effect, which is defined as a change in stress condition, in which material that is ordinarily
a solid behaves like a liquid can be considered as well. The LMF (Liquefaction Modification Factor)
values are implemented as multiplication factors to the median fragility values and they must be present
in the dataset.

The code covers Normal and LogNormal fragilities with 4 limit states (slight, moderate, extensive
and complete) and creates  an output CSV file.

**Required Parameters**

1. **Result name** A name for the result dataset, usually in CSV format which contains the damage information.
2. **Water facility Dataset ID** A water facility dataset you want to calculate damage for.
3. **Hazard Type** A hazard type for calculating water facility damage. E.g Earthquake
4. **Hazard ID** A hazard ID for calculating water facility damage.  Generally, hazards with PGA values are used to calculate water facility damages.
5. **Mapping ID** Default water facility fragility mapping on Incore-service. It implicitly defines the fragilities to be used in the calculation.


**Optional Parameters**

1. **Liquefaction** Use liquefaction to modify fragility curve. Default False. If True provide liquefaction geology dataset ID.
2. **Number of CPUs** Number of CPUs used for parallel computations. Default 1.
