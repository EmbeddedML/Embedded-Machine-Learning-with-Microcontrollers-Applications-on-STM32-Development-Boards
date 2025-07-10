/*
 * lib_hts221.h
 *
 *  Created on: Feb 18, 2023
 *      Author: Eren Atmaca
 */

#ifndef INC_LIB_HTS221_H_
#define INC_LIB_HTS221_H_

#include "hts221.h"
#include "stm32f7xx_hal.h"

extern I2C_HandleTypeDef hi2c1;

int8_t LIB_HTS221_Init(void);
int8_t LIB_HTS221_GetTemperature(float *temp);
int8_t LIB_HTS221_GetHumidity(float *hum);


#endif /* INC_LIB_HTS221_H_ */
