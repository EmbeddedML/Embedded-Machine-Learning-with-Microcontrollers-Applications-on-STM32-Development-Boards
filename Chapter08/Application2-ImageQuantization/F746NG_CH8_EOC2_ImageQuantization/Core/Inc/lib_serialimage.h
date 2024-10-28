/*
 * lib_serialimage.h
 *
 *  Created on: 29 Oca 2023
 *      Author: Eren Atmaca
 */

#ifndef INC_SERIAL_IMAGE_H_
#define INC_SERIAL_IMAGE_H_

#ifdef __cplusplus
extern "C" {
#endif

#include "stm32f7xx_hal.h"
#include "lib_image.h"

#define SERIAL_OK				((int8_t)0)
#define SERIAL_ERROR			((int8_t)-1)

#define __huart 			huart1
extern UART_HandleTypeDef 	__huart;


int8_t LIB_SERIAL_IMG_Transmit(IMAGE_HandleTypeDef * img);
int8_t LIB_SERIAL_IMG_Receive(IMAGE_HandleTypeDef * img);

#ifdef __cplusplus
}
#endif

#endif /* INC_SERIAL_IMAGE_H_ */
