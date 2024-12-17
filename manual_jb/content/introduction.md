# Introduction

The National Institute of Standards and Technology (NIST) funded the Center of Excellence for Risk-Based Community
Resilience Planning ([CoE](http://resilience.colostate.edu/)) (Cooperative Agreement 70NANB15H044), to develop the measurement science to support
community resilience assessment. The measurement science is implemented on a platform called <b>I</b>nterdependent <b>N</b>etworked <b>Co</b>mmunity <b>R</b>esilience Modeling <b>E</b>nvironment (**INCORE**). It incorporates a risk-based approach
to decision-making that enables quantitative comparisons of alternative resilience strategies.
On the IN-CORE platform, data from the community can be seamlessly integrated which allows users to optimize
community disaster resilience planning and post-disaster recovery strategies intelligently using physics-based
models of inter-dependent physical systems combined with socio-economic systems.

IN-CORE consists of multiple components as shown below:

![IN-CORE name and logo](images/incore.jpg)

**pyIncore**  is a Python package consisting of three primary components: 1) a set of service classes to interact
with the IN-CORE web services described below, 2) IN-CORE analyses and 3) visualization. The pyIncore allows users
to apply various hazards to infrastructure in selected areas, propagating the effect of physical infrastructure
damage and loss of functionality to social and economic impacts. Refer to [pyIncore section](pyincore.md) for detailed information.

**IN-CORE Web Services** are written in Java with JAX-RS specification and are comprised of a Hazard Service,
DFR3 (Damage, Functionality, Repair, Recovery, Restoration) Service, Data Service, Geospatial Visualization
Service, Semantic Service, and Space Service. These services allow users to create and access hazards, fragilities
and data. Users can access and utilize these services via pyIncore and IN-CORE Web Tools. For detailed information,
please refer to the [technical reference document](https://incore.ncsa.illinois.edu/doc/api/).

**IN-CORE Web Tools** is a set of web viewers for interacting with the different IN-CORE web services.
The viewers enable users to browse, search **Datasets**, **Hazards**, **Fragility curves**, **Repair curves**, etc.,
view the metadata and visualizations, and download items allowed.  For detailed information, please refer
to the [IN-CORE Web Tools section](webtools.md).

**IN-CORE Lab** is a customized Jupyter Lab with **pyIncore** installed and hosted on a NCSA cloud system.
It allows users to develop/run/test their scientific model with pyIncore in their own workspace.
Example Jupyter notebooks are provided with each pyincore analysis to help users get started and to help them
understand how to use the pyIncore.  For detailed information, please refer to the [IN-CORE Lab section](incore_lab.md).

Below you can find six Jupyter notebook [research examples](notebooks.md) that demonstrate IN-CORE:

1. [Galveston testbed](notebooks/Galveston_testbed/Galveston_testbed.md) ([zip](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/Galveston_testbed.zip) file).
2. [Joplin testbed](notebooks/Joplin_testbed/Joplin_testbed.md) ([zip](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/Joplin_testbed.zip) file).
3. [Lumberton testbed](notebooks/Lumberton_testbed/Lumberton_testbed.md) ([zip](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/Lumberton_testbed.zip) file).
4. [MMSA testbed Example 1](notebooks/MMSA_testbed/MMSA_Seismic_Functionality_Analysis_for_Interdependent_Buildings-Water-Power_using_Fragility_and_Repair_Rate_Curves.md) ([zip](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/MMSA_testbed_1.zip) file).
5. [MMSA testbed Example 2](notebooks/MMSA_testbed/MMSA_Seismic_Functionality_and_Restoration_Analysis_for_Interdependent_Buildings-Water-Power_using_Restoration_Curves.md) ([zip](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/MMSA_testbed_2.zip) file).
6. [Mobile testbed](notebooks/Mobile_testbed/Mobile_testbed.md) ([zip](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/Mobile_testbed.zip) file).
7. [Mobile testbed port](notebooks/Mobile_testbed_port/FTA_Mobile_testbed_port.md) ([zip](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/Mobile_testbed_port.zip) file).
8. [Seaside testbed](notebooks/Seaside_testbed/Seaside_testbed.md) ([zip](https://github.com/IN-CORE/incore-docs/blob/main/notebooks/Seaside_testbed.zip) file).

You can download and run each Jupyter notebook to see how IN-CORE is utilized and see the results from each testbed.

