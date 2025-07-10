/*
 * lib_bno055.h
 *
 *  Created on: Mar 10, 2023
 *      Author: Eren Atmaca
 */

#ifndef INC_LIB_BNO055_H_
#define INC_LIB_BNO055_H_

#include "stm32f7xx_hal.h"

typedef struct
{
	float accel[3];
	float gyro[3];
	float mag[3];
}BNO055_F32DataTypeDef;

#define __hi2c				hi2c1
extern I2C_HandleTypeDef 	__hi2c;


int8_t LIB_BNO055_Init(void);
int8_t LIB_BNO055_ReadAccelXYZ(float *x, float *y, float *z);
int8_t LIB_BNO055_ReadGyroXYZ(float *x, float *y, float *z);
int8_t LIB_BNO055_ReadMagXYZ(float *x, float *y, float *z);

#endif /* INC_LIB_BNO055_H_ */
