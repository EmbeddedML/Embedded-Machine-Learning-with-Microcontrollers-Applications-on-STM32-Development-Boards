/*
 * ks_feature_extraction.h
 *
 *  Created on: Mar 23, 2024
 *      Author: Eren Atmaca
 */

#ifndef INC_KS_FEATURE_EXTRACTION_H_
#define INC_KS_FEATURE_EXTRACTION_H_

#ifdef __cplusplus
extern "C" {
#endif

#ifdef STM32F746xx
#include "stm32f746xx.h"
#endif


#include "arm_math.h"


#define nbMelFilters 		20
#define nbDctOutputs 		13

#define SAMP_FREQ 			8000
#define MEL_LOW_FREQ 		20
#define MEL_HIGH_FREQ 		4000
#define fftLen 			 	1024


int8_t ks_mfcc_init(void);
int8_t ks_mfcc_extract_features(float32_t *input, float32_t *output);





#ifdef __cplusplus
}
#endif



#endif /* INC_KS_FEATURE_EXTRACTION_H_ */
