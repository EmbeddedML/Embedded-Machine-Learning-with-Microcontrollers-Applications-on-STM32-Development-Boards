/*
 * lib_rng.c
 *
 *  Created on: Sep 23, 2023
 *      Author: Eren Atmaca
 */

#include "lib_rng.h"

static RNG_HandleTypeDef __hrng = {.Instance = RNG,
		.State = HAL_RNG_STATE_READY,
		.Lock = HAL_UNLOCKED,
		.ErrorCode = HAL_RNG_ERROR_NONE
};

static void LIB_RNG_MspInit(void);

/**
  * @brief Activates the RNG peripheral
  * @retval None
  */
void LIB_RNG_Init(void)
{
	LIB_RNG_MspInit();
	HAL_RNG_Init(&__hrng);
}

/**
  * @brief Generates a random 32-bit number
  * @retval 32-bit random number
  */
uint32_t LIB_RNG_GetRandomNumber(void)
{
	return HAL_RNG_GetRandomNumber(&__hrng);
}

/**
  * @brief Initializes RNG hardware
  * @retval None
  */
static void LIB_RNG_MspInit(void)
{
    __HAL_RCC_RNG_CLK_ENABLE();
}
