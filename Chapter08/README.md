# Chapter 8 - CLUSTERING

## About This Chapter

The aim in clustering is grouping the data at hand based on its inherent characteristics. While performing this operation, labeled data is not used as in classification and regression. In order to fully explain the clustering concept, we will start with its definition. Then, we will introduce the k-means and DBSCAN clustering algorithms. These algorithms have different working principles. Hence, they provide different clusters for the same data at hand. While handling each clustering algorithm, we will first cover its theoretical background. Then, we will explore its formation in Python on PC. Afterward, we will introduce methods to deploy the formed clustering algorithm to the STM32 microcontroller. As end of chapter applications, we will provide solution to two real-life problems via clustering as fall detection and image quantization.

## Listings
<center>

| Description  | Code    |
|----------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| k-means clustering in Python                                                       | [![Code](../Images/py.png)](PythonScripts/train_clus_kmeans.py)   |
| Exporting the trained k-means clustering algorithm parameters                      | [![Code](../Images/py.png)](PythonScripts/export_clus_kmeans.py)  |
| Header file for the k-means clustering algorithm                                   | [![Code](../Images/C.png)](exported_models/kmeans_clus_config.h)  |
| Source file for the k-means clustering algorithm                                   | [![Code](../Images/C.png)](exported_models/kmeans_clus_config.c)  |
| k-means clustering algorithm test code for STM32CubeIDE                            | [![Code]()]()        |
| Python script for comparing k-means clustering results                             | [![Code](../Images/py.png)](PythonScripts/setup_clus_kmeans.py) |
| k-means clustering test code for Mbed Studio                                       | [![Code]()]()     |
| DBSCAN clustering in Python                                                        | [![Code](../Images/py.png)](PythonScripts/train_clus_dbscan.py)   |
| Exporting the trained DBSCAN clustering algorithm parameters                       | [![Code](../Images/py.png)](PythonScripts/export_clus_kmeans.py)  |
| Header file for the DBSCAN clustering algorithm                                    | [![Code](../Images/C.png)](exported_models/dbscan_clus_config.h)  |
| Source file for the DBSCAN clustering algorithm                                    | [![Code](../Images/C.png)](exported_models/dbscan_clus_config.c)  |
| DBSCAN clustering algorithm test code for STM32CubeIDE                             | [![Code]()]()     |
| Python script for comparing DBSCAN clustering results                              | [![Code](../Images/py.png)](PythonScripts/setup_clus_dbscan.py)   |
| DBSCAN clustering test code for Mbed Studio                                        | [![Code]()]()     |

</center>


## End of Chapter Applications

<!-- <center>

| Description                         | Python Scripts                                             |  Project Files                                        |
| ----------------------------------- | ---------------------------------------------------------- | ----------------------------------------------------- |
| Fall Detection                      | [![Code](../Images/py.png)]()      | [![Code]() |
| Image Quantization                  | [![Code](../Images/py.png)]()      | [![Code]() |

</center> -->

