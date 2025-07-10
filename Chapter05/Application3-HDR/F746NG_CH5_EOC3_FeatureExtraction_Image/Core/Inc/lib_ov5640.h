/*
 * lib_ov5640.h
 *
 *  Created on: 29 Oca 2023
 *      Author: Eren Atmaca
 */

#ifndef INC_LIB_OV5640_H_
#define INC_LIB_OV5640_H_

#ifdef __cplusplus
extern "C" {
#endif

#include "stm32f7xx_hal.h"
#include "ov5640.h"
#include "lib_image.h"


#define DCMI_D0_Pin             GPIO_PIN_9
#define DCMI_D0_GPIO_Port       GPIOH
#define DCMI_D1_Pin             GPIO_PIN_10
#define DCMI_D1_GPIO_Port       GPIOH
#define DCMI_D2_Pin             GPIO_PIN_11
#define DCMI_D2_GPIO_Port       GPIOH
#define DCMI_D3_Pin             GPIO_PIN_12
#define DCMI_D3_GPIO_Port       GPIOH
#define DCMI_D4_Pin             GPIO_PIN_14
#define DCMI_D4_GPIO_Port       GPIOH
#define DCMI_D5_Pin             GPIO_PIN_3
#define DCMI_D5_GPIO_Port       GPIOD
#define DCMI_D6_Pin             GPIO_PIN_5
#define DCMI_D6_GPIO_Port       GPIOE
#define DCMI_D7_Pin             GPIO_PIN_6
#define DCMI_D7_GPIO_Port       GPIOE
#define DCMI_VSYNC_Pin          GPIO_PIN_9
#define DCMI_VSYNC_GPIO_Port    GPIOG
#define DCMI_HSYNC_Pin          GPIO_PIN_4
#define DCMI_HSYNC_GPIO_Port    GPIOA
#define DCMI_PWR_EN_Pin         GPIO_PIN_13
#define DCMI_PWR_EN_GPIO_Port   GPIOH


typedef enum
{
	OV5640_RESOLUTION_R160x120 = OV5640_R160x120,
	OV5640_RESOLUTION_R320x240 = OV5640_R320x240,
	OV5640_RESOLUTION_R480x272 = OV5640_R480x272,
	OV5640_RESOLUTION_R640x480 = OV5640_R640x480,
	OV5640_RESOLUTION_R800x480 = OV5640_R800x480,
}LIB_OV5640_Resolution;

typedef enum
{
	OV5640_FORMAT_RGB565 	= OV5640_RGB565,
	OV5640_FORMAT_RGB888	= OV5640_RGB888,
	OV5640_FORMAT_YUV422 	= OV5640_YUV422,
	OV5640_FORMAT_Y8 		= OV5640_Y8,
	OV5640_FORMAT_JPEG 		= OV5640_JPEG,
}LIB_OV5640_Format;

int8_t LIB_OV5640_Init(LIB_OV5640_Resolution resolution, LIB_OV5640_Format format);
int8_t LIB_OV5640_StartContinuous(IMAGE_HandleTypeDef * img);
int8_t LIB_OV5640_CaptureSnapshot(IMAGE_HandleTypeDef * img, uint32_t timeout);
int8_t LIB_OV5640_Stop(void);
uint32_t LIB_OV5640_GetFrameCount(void);
void DCMI_IRQHandler(void);
void DMA2_Stream1_IRQHandler(void);

#ifdef __cplusplus
}
#endif

#endif /* INC_LIB_OV5640_H_ */
