#ifndef INC_KNN_INFERENCE_H_
#define INC_KNN_INFERENCE_H_


#ifdef __cplusplus
extern "C" {
#endif

#include "knn_reg_config.h"

int knn_reg_predict(float *input, float *output); //MODIFIED


#ifdef __cplusplus
}
#endif

#endif /* INC_KNN_INFERENCE_H_ */
