/*
 * kmeans_clus_inference.c
 *
 *  Created on: Apr 25, 2024
 *      Author: Berkan Höke, Eren Atmaca
 */

#include <math.h>
#include <float.h>
#include "kmeans_clus_inference.h"

static float euclid_distance(float *sample, float *target);

int8_t kmeans_clus_predict(float *input, float *output, bool online)
{
    float min_distance = FLT_MAX;
    int cluster_idx = -1;
    for (int i = 0; i < NUM_CLUSTERS; i++)
    {
        float cur_dist = euclid_distance(input, centroids[i]);
        if (cur_dist < min_distance)
        {
            min_distance = cur_dist;
            cluster_idx = i;
        }
    }

	if(online)
	{
		int num_samples = num_samples_per_cluster[cluster_idx];
		for(int i=0; i < NUM_FEATURES; i++)
		{
			float sum_feature = centroids[cluster_idx][i] * num_samples_per_cluster[cluster_idx];
			centroids[cluster_idx][i] = (input[i] + sum_feature) / (num_samples + 1);
		}
		num_samples_per_cluster[cluster_idx]++;
	}
	*output = cluster_idx;
    return 0;
}

static float euclid_distance(float *sample, float *target)
{
    float dist = 0;
    for (int i = 0; i < NUM_FEATURES; i++)
    {
        float diff = sample[i] - target[i];
        dist += diff * diff;
    }
    return sqrt(dist);
}
