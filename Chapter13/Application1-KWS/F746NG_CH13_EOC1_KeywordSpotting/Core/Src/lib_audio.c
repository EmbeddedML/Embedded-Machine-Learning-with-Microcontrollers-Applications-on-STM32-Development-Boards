/*
 * lib_audio.c
 *
 *  Created on: Aug 8, 2023
 *      Author: Eren Atmaca
 *
 *      Useful Notes:
 *      - This library is dependent on STM32F7 BSP audio driver.
 *      - If using CubeIDE, enable the SAI2, TIM1, and UART1 and disable the code generation
 *        from the CubeMX interface by deselecting the "Generate Code" checkboxs for
 *        MX_SAI2_Init and MX_TIM1_Init in Project Manager -> Advanced Settings -> Generated Function Calls
 *		- Firstly, start the recording with LIB_AUDIO_Init. Then, poll for recording with
 *		  LIB_AUDIO_PollForRecording. The recording will be automatically stopped after the buffer is
 *		  fully filled.
 */
#include "lib_audio.h"

#ifdef __MBED__
#include "BSP/STM32746G-Discovery/stm32746g_discovery_audio.h"
#else
#include "../../Drivers/BSP/STM32746G-Discovery/stm32746g_discovery_audio.h"
#endif

#define OK		((int8_t) 0)
#define ERROR	((int8_t)-1)

extern SAI_HandleTypeDef        haudio_in_sai;

static volatile uint8_t AudioRecordComplete = 0;
static volatile uint32_t __remaining 		= 0;
static uint16_t *__pRemaining;
static uint16_t *__pData;

/**
  * @brief Initializes SAI2 and CODEC for 16KHz audio frequency
  * @param None
  * @retval 0 if successfully initialized
  */
int8_t LIB_AUDIO_Init(void)
{
	if (BSP_AUDIO_IN_Init(AUDIO_FREQUENCY_16K, DEFAULT_AUDIO_IN_BIT_RESOLUTION, 1) != AUDIO_OK)
	{
		return ERROR;
	}
	return OK;
}

/**
  * @brief Starts the audio recording
  * @param pData   	Pointer to data buffer to be filled with audio data
  * @param length	Number of data in quantity (not bytes!)
  * @retval None
  */
void LIB_AUDIO_StartRecording(uint16_t *pData, uint32_t length)
{
	__remaining = length;
	__pRemaining = pData;
	__pData = pData;
	if (__remaining / UINT16_MAX)
	{
		BSP_AUDIO_IN_Record(pData, UINT16_MAX);
		__remaining = __remaining - UINT16_MAX;
		__pRemaining = __pRemaining + UINT16_MAX;
	}
	else
	{
		BSP_AUDIO_IN_Record(pData, __remaining);
		__remaining = 0;
	}
	AudioRecordComplete = 0;
}

/**
  * @brief Starts the audio recording
  * @note The timeout value must be large enough
  * @param timeout Timeout in milliseconds
  * @retval 0 if the audio data is successfully received
  * 		-1 if timeout occured
  */
int8_t LIB_AUDIO_PollForRecording(uint16_t timeout)
{
	uint32_t tick = HAL_GetTick();
	while(HAL_GetTick() - tick < timeout)
	{
		if (AudioRecordComplete == 1)
		{
			return OK;
		}
	}
	return ERROR;
}

/**
  * @brief Stops audio recording
  * @param None
  * @retval None
  */
void LIB_AUDIO_StopRecording(void)
{
	BSP_AUDIO_IN_Stop(CODEC_PDWN_SW);
}

/**
  * @brief Callback invoked by the HAL library when transfer is complete
  * @param None
  * @retval None
  */
void BSP_AUDIO_IN_TransferComplete_CallBack(void)
{
	BSP_AUDIO_IN_Stop(CODEC_PDWN_SW);
	if (__remaining / UINT16_MAX)
	{

		BSP_AUDIO_IN_Record(__pRemaining, UINT16_MAX);
		__pRemaining = __pRemaining + UINT16_MAX;
		__remaining = __remaining - UINT16_MAX;
	}
	else if(__remaining % UINT16_MAX)
	{
		BSP_AUDIO_IN_Record(__pRemaining, __remaining);
		__remaining = 0;
	}
	else
	{
		AudioRecordComplete = 1;
	}
}

/**
  * @brief DMA2 Stream 7 interrupt handler (DMA2_Stream7_IRQHandler)
  * @param None
  * @retval None
  */
void AUDIO_IN_SAIx_DMAx_IRQHandler(void)
{
	HAL_DMA_IRQHandler(haudio_in_sai.hdmarx);
}

