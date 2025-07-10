/*
 * lib_serial.c
 *
 *  Created on: Feb 19, 2023
 *      Author: Eren Atmaca
 */

#include "lib_serial.h"

/**
  * @brief Transmits the data with its data type information in packets
  * @param pData   	Pointer to data buffer of any type
  * @param length	Number of data in quantity (not bytes!)
  * @param type 	Choose from SERIAL_DataTypeDef enum
  * @retval 0 if successfully transmitted
  */
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

/**
  * @brief Receives the data in packets
  * @param pData   	Pointer to data buffer of any type
  * @param length	Number of data in quantity (not bytes!)
  * @param type 	Choose from SERIAL_DataTypeDef enum
  * @retval 0 if successfully received
  */
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

