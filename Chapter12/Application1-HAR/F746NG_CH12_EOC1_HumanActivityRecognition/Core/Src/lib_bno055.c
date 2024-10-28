/*
 * lib_bno055.c
 *
 *  Created on: Mar 10, 2023
 *      Author: Eren Atmaca
 */

#include "lib_bno055.h"
#include "bno055.h"

static int8_t __BNO055_Read(uint8_t dev_addr, uint8_t reg_addr, uint8_t *reg_data, uint8_t r_len);
static int8_t __BNO055_Write(uint8_t dev_addr, uint8_t reg_addr, uint8_t *reg_data, uint8_t r_len);
static void __BNO055_Delay(unsigned int millis);

static struct bno055_t bno055;

/**
  * @brief  Initializes the accelerometer, gyro and magnetometer
  * @param  None
  * @retval 0 if successfully initialized
  */
int8_t LIB_BNO055_Init(void)
{
	int8_t status;
	bno055.dev_addr = BNO055_I2C_ADDR1;
	bno055.bus_read = &__BNO055_Read;
	bno055.bus_write = &__BNO055_Write;
	bno055.delay_msec = &__BNO055_Delay;
	status = bno055_init(&bno055);
	status |= bno055_set_operation_mode(BNO055_OPERATION_MODE_AMG);
	return status;
}

/**
  * @brief  Reads the accelerometer.
  * @param  x Pointer to the accelerometer's x value.
  * @param  y Pointer to the accelerometer's y value.
  * @param  z Pointer to the accelerometer's z value.
  * @retval 0 if successfully read
  */
int8_t LIB_BNO055_ReadAccelXYZ(float *x, float *y, float *z)
{
	int8_t status;
	struct bno055_accel_float_t accel;
	status = bno055_convert_float_accel_xyz_mg(&accel);
	*x = accel.x;
	*y = accel.y;
	*z = accel.z;
	return status;
}

/**
  * @brief  Reads the gyro.
  * @param  x Pointer to the gyro's x value.
  * @param  y Pointer to the gyro's y value.
  * @param  z Pointer to the gyro's z value.
  * @retval 0 if successfully read
  */
int8_t LIB_BNO055_ReadGyroXYZ(float *x, float *y, float *z)
{
	int8_t status;
	struct bno055_gyro_float_t gyro;
	status = bno055_convert_float_gyro_xyz_dps(&gyro);
	*x = gyro.x;
	*y = gyro.y;
	*z = gyro.z;
	return status;
}

/**
  * @brief  Reads the magnetometer.
  * @param  x Pointer to the magnetometer's x value.
  * @param  y Pointer to the magnetometer's y value.
  * @param  z Pointer to the magnetometer's z value.
  * @retval 0 if successfully read
  */
int8_t LIB_BNO055_ReadMagXYZ(float *x, float *y, float *z)
{
	int8_t status;
	struct bno055_mag_float_t mag;
	status = bno055_convert_float_mag_xyz_uT(&mag);
	*x = mag.x;
	*y = mag.y;
	*z = mag.z;
	return status;
}

/**
 * @brief  Reads from BNO055 registers via I2C
 * @param  Address 	BNO055 I2C address
 * @param  Reg 		Internal register address
 * @param  pData 	Pointer to data
 * @param  Length 	Length of data
 * @retval 0 if successfully read
 */
static int8_t __BNO055_Read(uint8_t dev_addr, uint8_t reg_addr, uint8_t *reg_data, uint8_t r_len)
{
	return HAL_I2C_Mem_Read(&__hi2c, dev_addr << 1, reg_addr, I2C_MEMADD_SIZE_8BIT, reg_data, r_len, 1000);
}

/**
 * @brief  Writes to BNO055 registers via I2C
 * @param  Address 	BNO055 I2C address
 * @param  Reg 		Internal register address
 * @param  pData 	Pointer to data
 * @param  Length 	Length of data
 * @retval 0 if successfully written
 */
static int8_t __BNO055_Write(uint8_t dev_addr, uint8_t reg_addr, uint8_t *reg_data, uint8_t r_len)
{
	return HAL_I2C_Mem_Write(&__hi2c, dev_addr << 1, reg_addr, I2C_MEMADD_SIZE_8BIT, reg_data, r_len, 1000);
}

/**
 * @brief  Waits for milliseconds.
 * @param  millis Milliseconds to wait.
 * @retval None
 */
static void __BNO055_Delay(unsigned int millis)
{
	HAL_Delay(millis);
}
