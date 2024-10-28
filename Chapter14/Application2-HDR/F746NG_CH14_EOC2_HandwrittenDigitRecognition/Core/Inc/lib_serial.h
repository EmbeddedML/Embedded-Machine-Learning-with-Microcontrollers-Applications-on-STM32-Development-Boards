/*
 * lib_serial.h
 *
 *  Created on: Feb 19, 2023
 *      Author: Eren Atmaca
 */

#ifndef INC_LIB_SERIAL_H_
#define INC_LIB_SERIAL_H_

#ifdef __cplusplus
extern "C" {
#endif

#include "stm32f7xx_hal.h"

typedef enum
{
	TYPE_U8 	= 1,
	TYPE_S8 	= 2,
	TYPE_U16 	= 3,
	TYPE_S16 	= 4,
	TYPE_U32 	= 5,
	TYPE_S32 	= 6,
	TYPE_F32 	= 7,
}SERIAL_DataTypeDef;

#define SERIAL_OK				((int8_t)0)
#define SERIAL_ERROR			((int8_t)-1)

#define __huart					huart1
extern UART_HandleTypeDef		huart1;

int8_t LIB_SERIAL_Transmit(void *pData, uint32_t length, SERIAL_DataTypeDef type);
int8_t LIB_SERIAL_Receive(void *pData, uint32_t length, SERIAL_DataTypeDef type);

#ifdef __cplusplus
}
#endif

#endif /* INC_LIB_SERIAL_H_ */
