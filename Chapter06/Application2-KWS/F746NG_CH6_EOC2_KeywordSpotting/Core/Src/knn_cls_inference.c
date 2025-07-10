/*
 * knn_inference.h
 *
 *  Created on: Jan 22, 2022
 *      Author: berkan
 */

#include "knn_cls_inference.h"
#include <stdlib.h>
#include <string.h>


struct indexedArr
{
    float value;
    int index;
};

static float euclid_distance(const float *sample, const float *target);
static int compare(const void *a, const void *b);

int knn_cls_predict(float *input, int *output)
{
    struct indexedArr dists[NUM_SAMPLES];
    for (int i = 0; i < NUM_SAMPLES; i++)
    {
        dists[i].value = euclid_distance(DATA[i], input);
        dists[i].index = i;
    }

    qsort(dists, NUM_SAMPLES, sizeof(struct indexedArr), compare);

    int votes[NUM_CLASSES] = {0};
    for (int i = 0; i < NUM_NEIGHBORS; i++)
        votes[DATA_LABELS[dists[i].index]]++;

    memcpy(output, votes, NUM_CLASSES * sizeof(int));
    return 0;
}

static float euclid_distance(const float *sample, const float *target)
{
    float dist = 0;
    for (int i = 0; i < NUM_FEATURES; i++)
    {
        float diff = sample[i] - target[i];
        dist += diff * diff;
    }
    return dist;
}

static int compare(const void *a, const void *b)
{
    struct indexedArr *a1 = (struct indexedArr *)a;
    struct indexedArr *a2 = (struct indexedArr *)b;
    if ((*a1).value < (*a2).value)
        return -1;
    else if ((*a1).value > (*a2).value)
        return 1;
    else
        return 0;
}


