#ifndef KMEANS_CLUS_CONFIG_H_INCLUDED
#define KMEANS_CLUS_CONFIG_H_INCLUDED
#define NUM_CLUSTERS 8
#define NUM_FEATURES 2
extern int num_samples_per_cluster[NUM_CLUSTERS];
extern float centroids[NUM_CLUSTERS][NUM_FEATURES];
#endif