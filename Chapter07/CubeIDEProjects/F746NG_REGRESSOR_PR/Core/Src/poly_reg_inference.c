#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "poly_reg_inference.h"

int poly_reg_predict(float *input, float *output)
{
    float sum = OFFSET;
    for (int i = 0; i < NUM_FEATURES; i++)
    {
        //printf("i = %d\n", i);
        size_t feature_len = strlen(feature_names[i]);
        char *feature_copy = (char *)malloc(feature_len + 1);  // +1 for null terminator
        strcpy(feature_copy, feature_names[i]);
        char *token = strtok(feature_names[i], "*");
        float mult = COEFFS[i];

        while (token != NULL)
        {
            //printf("%s\n", token);
            int feature_num = atoi(token);
            mult *= input[feature_num];
            token = strtok(NULL, "*");
        }
        sum += mult;
        free(feature_copy);
    }
    *output = sum;
    return 0;
}
