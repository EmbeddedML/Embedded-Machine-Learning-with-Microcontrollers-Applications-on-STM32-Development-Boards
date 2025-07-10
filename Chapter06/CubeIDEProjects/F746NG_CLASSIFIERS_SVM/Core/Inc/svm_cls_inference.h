#ifndef INC_SVM_INFERENCE_H_
#define INC_SVM_INFERENCE_H_

#ifdef __cplusplus
extern "C" {
#endif

#include "svm_cls_config.h"

int svm_cls_predict(float* input, int* label);
int svm_cls_score(float* input, float* score);

#ifdef __cplusplus
}
#endif

#endif /* INC_SVM_INFERENCE_H_ */
