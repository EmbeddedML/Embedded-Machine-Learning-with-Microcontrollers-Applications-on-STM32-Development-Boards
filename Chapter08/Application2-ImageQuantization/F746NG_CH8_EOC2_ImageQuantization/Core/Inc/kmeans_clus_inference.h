/*
 * kmeans_clus_inference.h
 *
 *  Created on: Apr 25, 2024
 *      Author: Berkan Höke, Eren Atmaca
 */

#ifndef INC_KMEANS_CLUS_INFERENCE_H_
#define INC_KMEANS_CLUS_INFERENCE_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>
#include <stdbool.h>
#include "kmeans_clus_config.h"

int8_t kmeans_clus_predict(float *input, float *output, bool online);

#ifdef __cplusplus
}
#endif


#endif /* INC_KMEANS_CLUS_INFERENCE_H_ */
