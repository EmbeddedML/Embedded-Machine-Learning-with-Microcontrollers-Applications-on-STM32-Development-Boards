/*
 * hdr_feature_extraction.h
 *
 *  Created on: 24 Mar 2024
 *      Author: Eren Atmaca, Berkan Höke
 */

#ifndef INC_HDR_FEATURE_EXTRACTION_H_
#define INC_HDR_FEATURE_EXTRACTION_H_

#ifdef __cplusplus
extern "C" {
#endif


#include <stdint.h>
#include "lib_image.h"

typedef struct __HDR_FtrExtOutput
{
	float moments[4][4];
	float nu[4][4];
	float mu[4][4];
	float hu_moments[7];
}HDR_FtrExtOutput;

int8_t hdr_calculate_moments(IMAGE_HandleTypeDef * img, HDR_FtrExtOutput *output);
void hdr_calculate_hu_moments(HDR_FtrExtOutput *output);


#ifdef __cplusplus
}
#endif


#endif /* INC_HDR_FEATURE_EXTRACTION_H_ */
