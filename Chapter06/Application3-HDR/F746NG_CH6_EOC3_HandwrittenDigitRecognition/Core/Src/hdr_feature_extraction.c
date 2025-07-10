/*
 * hdr_feature_extraction.c
 *
 *  Created on: 24 Mar 2024
 *      Author: Eren Atmaca, Berkan Höke
 */

#include "hdr_feature_extraction.h"
#include "math.h"
#include "string.h"

int8_t hdr_calculate_moments(IMAGE_HandleTypeDef * img, HDR_FtrExtOutput *output)
{
	if (img->format != IMAGE_FORMAT_GRAYSCALE)
	{
		return -1;
	}
	memset(output, 0, sizeof(HDR_FtrExtOutput));
    for(uint32_t c = 0; c < img->width; c++)
    {
        for (uint32_t r = 0; r < img->height; r++)
        {
            for(uint32_t i = 0; i < 4; i++)
            {
                for(uint32_t j = 0; j < 4 - i; j++)
                {
                	output->moments[i][j] += powf((float)c, (float)i) * powf((float)r, (float)j) * ((float)(img->pData[c * img->height + r]) > 0.0f);
                }
            }
        }
    }

    float centroid_x = output->moments[1][0] / output->moments[0][0];
    float centroid_y = output->moments[0][1] / output->moments[0][0];
    output->mu[1][1] = fmaxf(output->moments[1][1] - centroid_x * output->moments[0][1],0);
    output->mu[2][0] = fmaxf(output->moments[2][0] - centroid_x * output->moments[1][0],0);
    output->mu[0][2] = fmaxf(output->moments[0][2] - centroid_y * output->moments[0][1],0);
    output->mu[3][0] = fmaxf(output->moments[3][0] - 3 * centroid_x * output->moments[2][0] + 2 * powf(centroid_x, 2) * output->moments[1][0], 0);
    output->mu[2][1] = fmaxf(output->moments[2][1] - 2 * centroid_x * output->moments[1][1] - centroid_y * output->moments[2][0] + 2 * powf(centroid_x, 2) * output->moments[0][1],0);
    output->mu[1][2] = fmaxf(output->moments[1][2] - 2 * centroid_y * output->moments[1][1] - centroid_x * output->moments[0][2] + 2 * powf(centroid_y, 2) * output->moments[1][0],0);
    output->mu[0][3] = fmaxf(output->moments[0][3] - 3 * centroid_y * output->moments[0][2] + 2 * powf(centroid_y, 2) * output->moments[0][1], 0);
    output->nu[2][0] = output->mu[2][0] / powf(output->moments[0][0], 2.0);
    output->nu[1][1] = output->mu[1][1] / powf(output->moments[0][0], 2.0);
    output->nu[0][2] = output->mu[0][2] / powf(output->moments[0][0], 2.0);
    output->nu[3][0] = output->mu[3][0] / powf(output->moments[0][0], 2.5);
    output->nu[2][1] = output->mu[2][1] / powf(output->moments[0][0], 2.5);
    output->nu[1][2] = output->mu[1][2] / powf(output->moments[0][0], 2.5);
    output->nu[0][3] = output->mu[0][3] / powf(output->moments[0][0], 2.5);
    return 0;
}


void hdr_calculate_hu_moments(HDR_FtrExtOutput *output)
{
	output->hu_moments[0] = output->nu[2][0] + output->nu[0][2];
	output->hu_moments[1] = powf(output->nu[2][0] - output->nu[0][2], 2) + 4 * powf(output->nu[1][1], 2);
	output->hu_moments[2] = powf(output->nu[3][0] -3 * output->nu[1][2], 2) + powf(3 * output->nu[2][1] - output->nu[0][3], 2);
	output->hu_moments[3] = powf(output->nu[3][0] + output->nu[1][2], 2) + powf(output->nu[2][1] + output->nu[0][3], 2);
	output->hu_moments[4] = (output->nu[3][0] - 3 * output->nu[1][2])
					* (output->nu[3][0] + output->nu[1][2])
					* (powf(output->nu[3][0] + output->nu[1][2], 2) - 3 * powf(output->nu[2][1] + output->nu[0][3], 2))
					+ (3 * output->nu[2][1] - output->nu[0][3])
					* (output->nu[2][1] + output->nu[0][3])
					* (3 * powf(output->nu[3][0] + output->nu[1][2], 2) - powf(output->nu[2][1] + output->nu[0][3],2));
	output->hu_moments[5] = (output->nu[2][0]- output->nu[0][2])
					* (powf(output->nu[3][0]+ output->nu[1][2],2) - powf(output->nu[2][1] + output->nu[0][3],2))
					+ 4 * output->nu[1][1] * (output->nu[3][0] + output->nu[1][2]) * (output->nu[2][1] + output->nu[0][3]);
	output->hu_moments[6] = (3 * output->nu[2][1] - output->nu[0][3])
					* (output->nu[3][0] + output->nu[1][2])
					* (powf(output->nu[3][0] + output->nu[1][2], 2) - 3 * powf(output->nu[2][1] + output->nu[0][3], 2))
					- (output->nu[3][0]-3 * output->nu[1][2]) * (output->nu[2][1] + output->nu[0][3]) * (3 * powf(output->nu[3][0] + output->nu[1][2],2) - powf(output->nu[2][1] + output->nu[0][3], 2));
}

