
/*
 * dbscan_clus_inference.h
 *
 *  Created on: Apr 25, 2024
 *      Author: Berkan Höke, Eren Atmaca
 */

#ifndef INC_DBSCAN_CLUS_INFERENCE_H_
#define INC_DBSCAN_CLUS_INFERENCE_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <math.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>
#include "dbscan_clus_config.h"

int8_t dbscan_clus_predict(float *input, int32_t *output);

#ifdef __cplusplus
}
#endif


#endif /* INC_DBSCAN_CLUS_INFERENCE_H_ */
