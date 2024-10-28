/*
 * knn_inference.h
 *
 *  Created on: Jan 22, 2022
 *      Author: berkan
 */

#ifndef INC_KNN_CLS_INFERENCE_H_
#define INC_KNN_CLS_INFERENCE_H_

#ifdef __cplusplus
extern "C" {
#endif

#include "knn_cls_config.h"

int knn_cls_predict(float *input, int *output);

#ifdef __cplusplus
}
#endif

#endif /* INC_KNN_CLS_INFERENCE_H_ */
