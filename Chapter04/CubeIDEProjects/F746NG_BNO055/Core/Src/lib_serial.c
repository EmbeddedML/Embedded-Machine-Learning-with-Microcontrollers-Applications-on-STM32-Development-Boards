/*
 * lib_serial.c
 *
 *  Created on: Feb 19, 2023
 *      Author: Eren Atmaca
 */

#include "lib_serial.h"

//static DMA_HandleTypeDef __dma;

int8_t LIB_SERIAL_Init(void)
{
	__huart.Instance 		= __INSTANCE;
	__huart.Init.BaudRate 	= 2000000;
	__huart.Init.WordLength = UART_WORDLENGTH_8B;
	__huart.Init.StopBits 	= UART_STOPBITS_1;
	__huart.Init.Parity 	= UART_PARITY_NONE;
	__huart.Init.Mode 		= UART_MODE_TX_RX;
	if (HAL_UART_Init(&__huart) != HAL_OK)
	{
		return SERIAL_ERROR;
	}
	return SERIAL_OK;
}

/* |'S'|'T'|'W'|TYPE|LEN0|LEN1|LEN2|LEN3|... DATA ...| */
int8_t LIB_SERIAL_Transmit(void *pData, uint32_t length, SERIAL_DataTypeDef type)
{
	uint8_t __header[3] = "STW", __count = 0;
	uint32_t __length = 0;
	uint16_t __quotient = 0, __remainder = 0;
	uint16_t divisor = UINT16_MAX;
	uint8_t * __pData = (uint8_t*) pData;
	if ((type == TYPE_S8) || (type == TYPE_U8))
	{
		__length = length;
	}
	else if ((type == TYPE_S16) || (type == TYPE_U16))
	{
		__length = length * 2;
	}
	else if ((type == TYPE_S32) || (type == TYPE_U32) || (type == TYPE_F32))
	{
		__length = length * 4;
	}
	else
	{
		return SERIAL_ERROR;
	}
	__quotient 	= __length / divisor;
	__remainder = __length % divisor;

	HAL_UART_Transmit(&__huart, __header, 3, 10);
	HAL_UART_Transmit(&__huart, (uint8_t*)&type, 1, 10);
	HAL_UART_Transmit(&__huart, (uint8_t*)&__length, 4, 10);
	HAL_Delay(1);

	while(__count < __quotient)
	{
		HAL_UART_Transmit(&__huart, __pData, UINT16_MAX, 1000);
		__count++;
		__pData += UINT16_MAX;
	}
	if (__remainder)
	{
		HAL_UART_Transmit(&__huart, __pData, __remainder, 1000);
	}
	HAL_Delay(1);
	return SERIAL_OK;
}

int8_t LIB_SERIAL_Receive(void *pData, uint32_t length, SERIAL_DataTypeDef type)
{
	uint8_t __header[3] = "STR", __count = 0;
	uint32_t __length = 0;
	uint16_t __quotient = 0, __remainder = 0;
	uint16_t divisor = UINT16_MAX;
	uint8_t * __pData = (uint8_t*) pData;
	if ((type == TYPE_S8) || (type == TYPE_U8))
	{
		__length = length;
	}
	else if ((type == TYPE_S16) || (type == TYPE_U16))
	{
		__length = length * 2;
	}
	else if ((type == TYPE_S32) || (type == TYPE_U32) || (type == TYPE_F32))
	{
		__length = length * 4;
	}
	else
	{
		return SERIAL_ERROR;
	}
	__quotient 	= __length / divisor;
	__remainder = __length % divisor;

	HAL_UART_Transmit(&__huart, __header, 3, 10);
	HAL_UART_Transmit(&__huart, (uint8_t*)&type, 1, 10);
	HAL_UART_Transmit(&__huart, (uint8_t*)&__length, 4, 10);
	HAL_Delay(1);

	while(__count < __quotient)
	{
		if(HAL_UART_Receive(&__huart, __pData, UINT16_MAX, 10000) != HAL_OK)
		{
			return SERIAL_ERROR;
		}
		__count++;
		__pData += UINT16_MAX;
	}
	if (__remainder)
	{
		if(HAL_UART_Receive(&__huart, __pData, __remainder, 10000) != HAL_OK)
		{
			return SERIAL_ERROR;
		}
	}
	HAL_Delay(1);
	return SERIAL_OK;
}

