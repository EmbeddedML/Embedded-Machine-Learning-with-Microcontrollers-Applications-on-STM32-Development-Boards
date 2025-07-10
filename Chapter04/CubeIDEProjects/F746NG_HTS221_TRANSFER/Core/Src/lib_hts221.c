/*
 * lib_hts221.c
 *
 *  Created on: Feb 18, 2023
 *      Author: Eren Atmaca
 */

#include "lib_hts221.h"

static HTS221_Object_t hts221;
static int32_t __HTS221_ReadReg(uint16_t Address, uint16_t Reg, uint8_t * pData, uint16_t Length);
static int32_t __HTS221_WriteReg(uint16_t Address, uint16_t Reg, uint8_t * pData, uint16_t Length);
static int32_t __HTS221_Init(void);
static int32_t __HTS221_GetTick(void);


/**
  * @brief  Initializes the HTS221 library and both (humidity and temperature) sensors.
  * @retval 0 if successfully initialized
  */
int8_t LIB_HTS221_Init(void)
{
	int8_t status;
	HTS221_IO_t __htsIO;
	__htsIO.BusType = HTS221_I2C_BUS;
	__htsIO.Address = 0xBE;
	__htsIO.GetTick = &__HTS221_GetTick;
	__htsIO.Init	= &__HTS221_Init;
	__htsIO.ReadReg = &__HTS221_ReadReg;
	__htsIO.WriteReg = &__HTS221_WriteReg;
	status = HTS221_RegisterBusIO(&hts221, &__htsIO);
	status |= HTS221_HUM_Enable(&hts221);
	status |= HTS221_TEMP_Enable(&hts221);
	return status;
}

/**
  * @brief  Reads the temperature.
  * @param  temp Pointer to the temperature value.
  * @retval 0 if successfully read
  */
int8_t LIB_HTS221_GetTemperature(float *temp)
{
	int8_t status;
	HTS221_TEMP_Get_DRDY_Status(&hts221, (uint8_t*)&status);
	if (!status)
	{
		return HTS221_ERROR;
	}
	HTS221_TEMP_GetTemperature(&hts221, temp);
	return HTS221_OK;
}

/**
  * @brief  Reads the humidity.
  * @param  temp Pointer to the humidity value.
  * @retval 0 if successfully read
  */
int8_t LIB_HTS221_GetHumidity(float *hum)
{
	int8_t status;
	HTS221_HUM_Get_DRDY_Status(&hts221, (uint8_t*)&status);
	if (!status)
	{
		return HTS221_ERROR;
	}
	HTS221_HUM_GetHumidity(&hts221, hum);
	return HTS221_OK;
}

/**
 * @brief  Reads from HTS221 registers via I2C
 * @param  Address 	HTS221 I2C address
 * @param  Reg 		Internal register address
 * @param  pData 	Pointer to data
 * @param  Length 	Length of data
 * @retval 0 if successfully read
 */
static int32_t __HTS221_ReadReg(uint16_t Address, uint16_t Reg, uint8_t * pData, uint16_t Length)
{
	return HAL_I2C_Mem_Read(&hi2c1, (Address | 0x01), Reg, I2C_MEMADD_SIZE_8BIT, pData, Length, 1000);
}

/**
 * @brief  Writes to HTS221 registers via I2C
 * @param  Address 	HTS221 I2C address
 * @param  Reg 		Internal register address
 * @param  pData 	Pointer to data
 * @param  Length 	Length of data
 * @retval 0 if successfully written
 */
static int32_t __HTS221_WriteReg(uint16_t Address, uint16_t Reg, uint8_t * pData, uint16_t Length)
{
	return HAL_I2C_Mem_Write(&hi2c1, Address, Reg, I2C_MEMADD_SIZE_8BIT, pData, Length, 1000);
}

/**
 * @brief  Initializes HTS221.
 * @retval 0 if successfully written
 */
static int32_t __HTS221_Init(void)
{
	return HTS221_Init(&hts221);
}

/**
 * @brief  Reads the current tick value
 * @retval The current tick
 */
static int32_t __HTS221_GetTick(void)
{
	return (int32_t)HAL_GetTick();
}
