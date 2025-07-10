#include "dt_reg_inference.h"

int dt_reg_predict(float *input, float *output)
{
    int idx = 0; // Root Node
    while (idx >= 0)
    {
        float feature_val = input[SPLIT_FEATURE[idx]];
        if (SPLIT_FEATURE[idx] < 0)
        {
        	*output = VALUES[idx];
			return 0;
        }
        if (feature_val < THRESHOLDS[idx])
            idx = LEFT_CHILDREN[idx];
        else
            idx = RIGHT_CHILDREN[idx];
    }
    return -1;
}
