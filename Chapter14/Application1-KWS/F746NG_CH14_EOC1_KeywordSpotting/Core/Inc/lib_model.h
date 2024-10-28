/*
 * lib_model.h
 *
 *  Created on: Oct 14, 2023
 *      Author: Eren Atmaca
 */

#ifndef INC_LIB_MODEL_H_
#define INC_LIB_MODEL_H_

#ifndef TF_LITE_STATIC_MEMORY
#define TF_LITE_STATIC_MEMORY
#endif

#include "stdint.h"
#include "tensorflow/lite/c/common.h"
#include "tensorflow/lite/micro/tflite_bridge/micro_error_reporter.h"
#include "tensorflow/lite/micro/micro_interpreter.h"
#include "tensorflow/lite/micro/micro_mutable_op_resolver.h"
#include "tensorflow/lite/schema/schema_generated.h"

#define OK		(0)
#define ERROR	(-1)

int8_t LIB_MODEL_Init(const void *tfliteModel, TfLiteTensor **inputTensor, uint8_t *buffer, uint32_t bufferSize);
int8_t LIB_MODEL_Run(TfLiteTensor **output);


#endif /* INC_LIB_MODEL_H_ */
