/*
 * kmeans_clus_inference.c
 *
 *  Created on: Apr 25, 2024
 *      Author: Berkan Höke, Eren Atmaca
 */

#include <float.h>
#include "dbscan_clus_inference.h"

static float euclid_distance(float *sample, float *target);

int8_t dbscan_clus_predict(float *input, int32_t *output)
{
	int32_t cur_label_idx = 0;
	int32_t label = -1;
    float min_distance = FLT_MAX;
    for (int32_t i = 0; i < NUM_CORE_POINTS; i++)
    {
        float cur_dist = euclid_distance(input, CORE_POINTS[i]);
        if (cur_dist < min_distance)
        {
            min_distance = cur_dist;
            cur_label_idx = i;
        }
    }
    
    if (min_distance < EPS)
        label = LABELS[cur_label_idx];

    *output = label;
    return 0;
}


static float euclid_distance(float *sample, float *target)
{
    float dist = 0;
    for (int32_t i = 0; i < NUM_FEATURES; i++)
    {
        float diff = sample[i] - target[i];
        dist += diff * diff;
    }
    return sqrt(dist);
}
