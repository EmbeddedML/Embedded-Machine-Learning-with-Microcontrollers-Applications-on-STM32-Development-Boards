#include "dt_cls_inference.h"
#include <stdio.h>
#include <string.h>

/**
  * @brief Run inference using decision tree
  * @param input	Pointer to an array of NUM_FEATURES length
  * @param output	Pointer to an array of NUM_CLASSES length
  * @retval 0 if successful inference
  */
int dt_cls_predict(float *input, int *output)
{
    int idx = 0; // Root Node
    while (idx >= 0)
    {
        float feature_val = input[SPLIT_FEATURE[idx]];
        if (SPLIT_FEATURE[idx] < 0)
        {
        	memcpy(output, VALUES[idx], NUM_CLASSES * sizeof(int));
        	return 0;
        }
        if (feature_val < THRESHOLDS[idx])
            idx = LEFT_CHILDREN[idx];
        else
            idx = RIGHT_CHILDREN[idx];
    }
    return -1;
}
