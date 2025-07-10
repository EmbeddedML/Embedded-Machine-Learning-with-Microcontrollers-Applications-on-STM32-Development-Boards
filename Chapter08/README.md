# Chapter 8 - CLUSTERING

## About This Chapter

The aim in clustering is grouping the data at hand based on its inherent characteristics. While performing this operation, labeled data is not used as in classification and regression. In order to fully explain the clustering concept, we will start with its definition. Then, we will introduce the k-means and DBSCAN clustering algorithms. These algorithms have different working principles. Hence, they provide different clusters for the same data at hand. While handling each clustering algorithm, we will first cover its theoretical background. Then, we will explore its formation in Python on PC. Afterward, we will introduce methods to deploy the formed clustering algorithm to the STM32 microcontroller. As end of chapter applications, we will provide solution to two real-life problems via clustering as fall detection and image quantization.

## Listings
<center>

| Description                                            | Code                                                                                                         |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| k-means clustering in Python                           | [![Code](../Images/py.png)](PythonScripts/train_clus_kmeans.py)                                              |
| Exporting the trained k-means clustering parameters    | [![Code](../Images/py.png)](PythonScripts/export_clus_kmeans.py)                                             |
| Header file for the k-means clustering                 | [![Code](../Images/C.png)](Chapter08/CubeIDEProjects/F746NG_CLUSTERING_KMEANS/Core/Inc/kmeans_clus_config.h) |
| Source file for the k-means clustering                 | [![Code](../Images/C.png)](Chapter08/CubeIDEProjects/F746NG_CLUSTERING_KMEANS/Core/Src/kmeans_clus_config.c) |
| k-means clustering CubeIDE project                     | [![Code](../Images/stm32.png)](Chapter08/CubeIDEProjects/F746NG_CLUSTERING_KMEANS)                           |
| Python script for comparing k-means clustering results | [![Code](../Images/py.png)](PythonScripts/setup_clus_kmeans.py)                                              |
| k-means clustering test code for Mbed Studio           | [![Code]()]()                                                                                                |
| DBSCAN clustering in Python                            | [![Code](../Images/py.png)](PythonScripts/train_clus_dbscan.py)                                              |
| Exporting the trained DBSCAN clustering parameters     | [![Code](../Images/py.png)](PythonScripts/export_clus_kmeans.py)                                             |
| Header file for the DBSCAN clustering                  | [![Code](../Images/C.png)](Chapter08/CubeIDEProjects/F746NG_CLUSTERING_DBSCAN/Core/Inc/dbscan_clus_config.h) |
| Source file for the DBSCAN clustering                  | [![Code](../Images/C.png)](Chapter08/CubeIDEProjects/F746NG_CLUSTERING_DBSCAN/Core/Src/dbscan_clus_config.h) |
| DBSCAN clustering test code for STM32CubeIDE           | [![Code](../Images/stm32.png)](Chapter08/CubeIDEProjects/F746NG_CLUSTERING_DBSCAN)                           |
| Python script for comparing DBSCAN clustering results  | [![Code](../Images/py.png)](PythonScripts/setup_clus_dbscan.py)                                              |
| DBSCAN clustering test code for Mbed Studio            | [![Code]()]()                                                                                                |

</center>


## End of Chapter Applications

<center>

| Description        | Python Scripts                                                  | Project Files                                                                                              |
| ------------------ | --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Fall Detection     | [![Code](../Images/py.png)](Chapter08/Application1-HAR/main.py) | [![Code](../Images/stm32.png)](Chapter08/Application1-HAR/F746NG_CH8_EOC1_FallDetection)                   |
| Image Quantization | [![Code](../Images/py.png)](Chapter08/Application2-IQ/main.py)  | [![Code](../Images/stm32.png)](Chapter08/Application2-ImageQuantization/F746NG_CH8_EOC2_ImageQuantization) |

</center>

