/*
 * lib_rng.h
 *
 *  Created on: Sep 23, 2023
 *      Author: Eren Atmaca
 */

#ifndef INC_LIB_RNG_H_
#define INC_LIB_RNG_H_

#ifdef __cplusplus
extern "C" {
#endif

#include "stm32f7xx_hal.h"

void LIB_RNG_Init(void);
uint32_t LIB_RNG_GetRandomNumber(void);

#ifdef __cplusplus
}
#endif

#endif /* INC_LIB_RNG_H_ */
