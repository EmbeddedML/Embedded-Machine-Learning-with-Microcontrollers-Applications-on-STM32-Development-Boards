#include "linear_reg_inference.h"

int linear_reg_predict(float *input, float *output)
{
    float sum = OFFSET;
    for (int i = 0; i < NUM_FEATURES; i++)
    {
        sum += COEFFS[i] * input[i];
    }
    *output = sum;
    return 0;
}
