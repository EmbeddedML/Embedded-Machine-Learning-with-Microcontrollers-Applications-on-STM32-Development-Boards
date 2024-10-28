/*
 * lib_ov5640.c
 *
 *  Created on: 29 Oca 2023
 *      Author: Eren Atmaca
 *
 *  Please note that this library is dependent on ST Microelectronics' ov5640 driver which you can find at:
 *  https://github.com/STMicroelectronics/stm32-ov5640
 *
 */


#include "lib_ov5640.h"

static OV5640_Object_t ov5640;
static volatile uint32_t ov5640FrameCount = 0;

static void LIB_DMA_Init(void);
static int8_t LIB_DCMI_Init(void);
static int8_t LIB_I2C1_Init(void);
static void LIB_DCMI_MspInit(DCMI_HandleTypeDef* __hdcmi);
static void LIB_I2C_MspInit(I2C_HandleTypeDef* hi2c);

static int32_t __OV5640_ReadReg_Func(uint16_t devAddr, uint16_t Reg, uint8_t* pData, uint16_t Length);
static int32_t __OV5640_WriteReg_Func(uint16_t devAddr, uint16_t Reg, uint8_t* pData, uint16_t Length);
static int32_t __OV5640_GetTick_Func(void);

DCMI_HandleTypeDef __hdcmi;
DMA_HandleTypeDef __hdma_dcmi;
I2C_HandleTypeDef hi2c1;

/**
  * @brief  Initializes the OV5640 library and the camera.
  * @param  resolution from LIB_OV5640_Resolution enum
  * @param  format	from LIB_OV5640_Format enum
  * @retval 0 if successfully initialized
  */
int8_t LIB_OV5640_Init(LIB_OV5640_Resolution resolution, LIB_OV5640_Format format)
{
	LIB_DMA_Init();
	LIB_DCMI_MspInit(&__hdcmi);
	LIB_DCMI_Init();
	LIB_I2C_MspInit(&hi2c1);
	LIB_I2C1_Init();
	ov5640.IO.WriteReg = __OV5640_WriteReg_Func;
	ov5640.IO.ReadReg  = __OV5640_ReadReg_Func;
	ov5640.IO.GetTick  = __OV5640_GetTick_Func;
	ov5640.IO.Address  = 0x78U;
	OV5640_RegisterBusIO(&ov5640, &ov5640.IO);
	return OV5640_Init(&ov5640, resolution, format);
}

/**
  * @brief  Starts the DCMI module for continuous capture.
  * @param  img pointer to image object
  * @retval 0 if successfully started
  */
int8_t LIB_OV5640_StartContinuous(IMAGE_HandleTypeDef * img)
{
	return HAL_DCMI_Start_DMA(&__hdcmi, DCMI_MODE_CONTINUOUS, (uint32_t)img->pData, img->size);
}

/**
  * @brief  Starts the DCMI module for only one shot.
  * @param  img pointer to image object
  * @param  timeout max time allowed in ms to capture one shot
  * @retval 0 if successfully captured
  */
int8_t LIB_OV5640_CaptureSnapshot(IMAGE_HandleTypeDef * img, uint32_t timeout)
{
	int8_t status = OV5640_ERROR;
	uint32_t currentFrameCount = ov5640FrameCount, currentTick;
	HAL_DCMI_Start_DMA(&__hdcmi, DCMI_MODE_CONTINUOUS, (uint32_t)img->pData, img->size);
	currentTick = HAL_GetTick();
	while((HAL_GetTick() - currentTick) < timeout)
	{
		if ((ov5640FrameCount - currentFrameCount) > 4)
		{
			status = OV5640_OK;
			break;
		}
	}
	HAL_DCMI_Stop(&__hdcmi);
	return status;
}

/**
  * @brief  Stops the DCMI module.
  * @retval 0 if successfully captured
  */
int8_t LIB_OV5640_Stop(void)
{
	return HAL_DCMI_Stop(&__hdcmi);
}

/**
  * @brief  returns the total number of captured frames.
  * @retval total number of captured frames.
  */
uint32_t LIB_OV5640_GetFrameCount(void)
{
	return ov5640FrameCount;
}

void HAL_DCMI_FrameEventCallback(DCMI_HandleTypeDef *__hdcmi)
{
	ov5640FrameCount++;
}

/**
  * Enable DMA controller clock
  */
static void LIB_DMA_Init(void)
{

  /* DMA controller clock enable */
  __HAL_RCC_DMA2_CLK_ENABLE();

  /* DMA interrupt init */
  /* DMA2_Stream1_IRQn interrupt configuration */
  HAL_NVIC_SetPriority(DMA2_Stream1_IRQn, 15, 0);
  HAL_NVIC_EnableIRQ(DMA2_Stream1_IRQn);

}

/**
  * @brief This function handles DMA2 stream1 global interrupt.
  */
void DMA2_Stream1_IRQHandler(void)
{
    HAL_DMA_IRQHandler(&__hdma_dcmi);
}

/**
  * @brief DCMI Initialization Function
  * @param None
  * @retval None
  */
static int8_t LIB_DCMI_Init(void)
{
    __hdcmi.Instance = DCMI;
    __hdcmi.Init.SynchroMode = DCMI_SYNCHRO_HARDWARE;
    __hdcmi.Init.PCKPolarity = DCMI_PCKPOLARITY_RISING;
    __hdcmi.Init.VSPolarity = DCMI_VSPOLARITY_HIGH;
    __hdcmi.Init.HSPolarity = DCMI_HSPOLARITY_HIGH;
    __hdcmi.Init.CaptureRate = DCMI_CR_ALL_FRAME;
    __hdcmi.Init.ExtendedDataMode = DCMI_EXTEND_DATA_8B;
    __hdcmi.Init.JPEGMode = DCMI_JPEG_DISABLE;
    __hdcmi.Init.ByteSelectMode = DCMI_BSM_ALL;
    __hdcmi.Init.ByteSelectStart = DCMI_OEBS_ODD;
    __hdcmi.Init.LineSelectMode = DCMI_LSM_ALL;
    __hdcmi.Init.LineSelectStart = DCMI_OELS_ODD;
    return HAL_DCMI_Init(&__hdcmi);
}


/**
* @brief DCMI MSP Initialization
* This function configures the hardware resources used in this example
* @param __hdcmi: DCMI handle pointer
* @retval None
*/
static void LIB_DCMI_MspInit(DCMI_HandleTypeDef* __hdcmi)
{
	GPIO_InitTypeDef GPIO_InitStruct = {0};
	/* Peripheral clock enable */
	__HAL_RCC_DCMI_CLK_ENABLE();

	__HAL_RCC_GPIOE_CLK_ENABLE();
	__HAL_RCC_GPIOD_CLK_ENABLE();
	__HAL_RCC_GPIOG_CLK_ENABLE();
	__HAL_RCC_GPIOH_CLK_ENABLE();
	__HAL_RCC_GPIOA_CLK_ENABLE();

	GPIO_InitStruct.Pin = DCMI_D6_Pin|DCMI_D7_Pin;
	GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
	GPIO_InitStruct.Pull = GPIO_NOPULL;
	GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
	GPIO_InitStruct.Alternate = GPIO_AF13_DCMI;
	HAL_GPIO_Init(GPIOE, &GPIO_InitStruct);

	GPIO_InitStruct.Pin = DCMI_D5_Pin;
	GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
	GPIO_InitStruct.Pull = GPIO_NOPULL;
	GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
	GPIO_InitStruct.Alternate = GPIO_AF13_DCMI;
	HAL_GPIO_Init(DCMI_D5_GPIO_Port, &GPIO_InitStruct);

	GPIO_InitStruct.Pin = DCMI_VSYNC_Pin;
	GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
	GPIO_InitStruct.Pull = GPIO_NOPULL;
	GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
	GPIO_InitStruct.Alternate = GPIO_AF13_DCMI;
	HAL_GPIO_Init(DCMI_VSYNC_GPIO_Port, &GPIO_InitStruct);

	GPIO_InitStruct.Pin = DCMI_D4_Pin|DCMI_D3_Pin|DCMI_D0_Pin|DCMI_D2_Pin
							|DCMI_D1_Pin;
	GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
	GPIO_InitStruct.Pull = GPIO_NOPULL;
	GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
	GPIO_InitStruct.Alternate = GPIO_AF13_DCMI;
	HAL_GPIO_Init(GPIOH, &GPIO_InitStruct);

	GPIO_InitStruct.Pin = DCMI_HSYNC_Pin|GPIO_PIN_6;
	GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
	GPIO_InitStruct.Pull = GPIO_NOPULL;
	GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
	GPIO_InitStruct.Alternate = GPIO_AF13_DCMI;
	HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

	/* DCMI DMA Init */
	/* DCMI Init */
	__hdma_dcmi.Instance = DMA2_Stream1;
	__hdma_dcmi.Init.Channel = DMA_CHANNEL_1;
	__hdma_dcmi.Init.Direction = DMA_PERIPH_TO_MEMORY;
	__hdma_dcmi.Init.PeriphInc = DMA_PINC_DISABLE;
	__hdma_dcmi.Init.MemInc = DMA_MINC_ENABLE;
	__hdma_dcmi.Init.PeriphDataAlignment = DMA_PDATAALIGN_WORD;
	__hdma_dcmi.Init.MemDataAlignment = DMA_MDATAALIGN_WORD;
	__hdma_dcmi.Init.Mode = DMA_CIRCULAR;
	__hdma_dcmi.Init.Priority = DMA_PRIORITY_HIGH;
	__hdma_dcmi.Init.FIFOMode = DMA_FIFOMODE_DISABLE;
	if (HAL_DMA_Init(&__hdma_dcmi) != HAL_OK)
	{
		return;
	}

	__HAL_LINKDMA(__hdcmi,DMA_Handle,__hdma_dcmi);

	/* DCMI interrupt Init */
	HAL_NVIC_SetPriority(DCMI_IRQn, 15, 0);
	HAL_NVIC_EnableIRQ(DCMI_IRQn);

}


/**
  * @brief I2C1 Initialization Function
  * @param None
  * @retval None
  */
static int8_t LIB_I2C1_Init(void)
{
	hi2c1.Instance = I2C1;
	hi2c1.Init.Timing = 0x00A0A3F7;
	hi2c1.Init.OwnAddress1 = 0;
	hi2c1.Init.AddressingMode = I2C_ADDRESSINGMODE_7BIT;
	hi2c1.Init.DualAddressMode = I2C_DUALADDRESS_DISABLE;
	hi2c1.Init.OwnAddress2 = 0;
	hi2c1.Init.OwnAddress2Masks = I2C_OA2_NOMASK;
	hi2c1.Init.GeneralCallMode = I2C_GENERALCALL_DISABLE;
	hi2c1.Init.NoStretchMode = I2C_NOSTRETCH_DISABLE;
	return HAL_I2C_Init(&hi2c1);
}


/**
* @brief I2C MSP Initialization
* This function configures the hardware resources used in this example
* @param hi2c: I2C handle pointer
* @retval None
*/
static void LIB_I2C_MspInit(I2C_HandleTypeDef* hi2c)
{
	GPIO_InitTypeDef GPIO_InitStruct = {0};
	RCC_PeriphCLKInitTypeDef PeriphClkInitStruct = {0};
	/** Initializes the peripherals clock
	*/
	PeriphClkInitStruct.PeriphClockSelection = RCC_PERIPHCLK_I2C1;
	PeriphClkInitStruct.I2c1ClockSelection = RCC_I2C1CLKSOURCE_PCLK1;
	if (HAL_RCCEx_PeriphCLKConfig(&PeriphClkInitStruct) != HAL_OK)
	{
	  return;
	}

	__HAL_RCC_GPIOB_CLK_ENABLE();
	/**I2C1 GPIO Configuration
	PB8     ------> I2C1_SCL
	PB9     ------> I2C1_SDA
	*/
	GPIO_InitStruct.Pin = GPIO_PIN_8|GPIO_PIN_9;
	GPIO_InitStruct.Mode = GPIO_MODE_AF_OD;
	GPIO_InitStruct.Pull = GPIO_NOPULL;
	GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_LOW;
	GPIO_InitStruct.Alternate = GPIO_AF4_I2C1;
	HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

	/* Peripheral clock enable */
	__HAL_RCC_I2C1_CLK_ENABLE();

}

/**
  * @brief This function handles DCMI global interrupt.
  */
void DCMI_IRQHandler(void)
{
    HAL_DCMI_IRQHandler(&__hdcmi);
}


/**
  * @brief  reads OV5640 registers.
  * @retval 0 if successfully read.
  */
static int32_t __OV5640_ReadReg_Func(uint16_t devAddr, uint16_t Reg, uint8_t* pData, uint16_t Length)
{
	return HAL_I2C_Mem_Read(&hi2c1, devAddr , Reg, I2C_MEMADD_SIZE_16BIT, pData, Length, 1000);
}

/**
  * @brief  writes to OV5640 registers.
  * @retval 0 if successfully written.
  */
static int32_t __OV5640_WriteReg_Func(uint16_t devAddr, uint16_t Reg, uint8_t* pData, uint16_t Length)
{
	return HAL_I2C_Mem_Write(&hi2c1, devAddr, Reg, I2C_MEMADD_SIZE_16BIT, pData, Length, 1000);
}

/**
  * @brief  returns the current tick value.
  * @retval the current tick value.
  */
static int32_t __OV5640_GetTick_Func(void)
{
	return (int32_t)HAL_GetTick();
}

