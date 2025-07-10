/*
 * lib_bayes.h
 *
 *  Created on: Oct 6, 2023
 *     Authors: Berkan Höke, Eren Atmaca
 */

#ifndef INC_BAYES_CLS_INFERENCE_H_
#define INC_BAYES_CLS_INFERENCE_H_

#ifdef __cplusplus
extern "C" {
#endif

#ifdef STM32F746xx
#include "stm32f746xx.h"
#endif

#include "arm_math.h"
#include "bayes_cls_config.h"

int8_t bayes_cls_predict(arm_matrix_instance_f32 *input, arm_matrix_instance_f32 *output);


#ifdef __cplusplus
}
#endif


#endif /* INC_BAYES_CLS_INFERENCE_H_ */
