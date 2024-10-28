#ifndef DTC_INFERENCE_H_INCLUDED
#define DTC_INFERENCE_H_INCLUDED

#ifdef __cplusplus
extern "C" {
#endif

#include "dt_cls_config.h"

int dt_cls_predict(float *input, int *output);

#ifdef __cplusplus
}
#endif

#endif
