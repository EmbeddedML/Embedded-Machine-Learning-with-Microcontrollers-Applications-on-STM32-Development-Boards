/*
 * lib_image.h
 *
 *  Created on: 29 Oca 2023
 *      Author: Eren Atmaca
 */

#ifndef INC_LIB_IMAGE_H_
#define INC_LIB_IMAGE_H_

#ifdef __cplusplus
extern "C" {
#endif


#include "stm32f7xx_hal.h"

#define IMAGE_OK							((int8_t)0)
#define IMAGE_ERROR							((int8_t)-1)
#define IMAGE_RESOLUTION_VGA_WIDTH			((uint16_t)640)
#define IMAGE_RESOLUTION_VGA_HEIGHT			((uint16_t)480)
#define IMAGE_RESOLUTION_QVGA_WIDTH			((uint16_t)320)
#define IMAGE_RESOLUTION_QVGA_HEIGHT		((uint16_t)240)
#define IMAGE_RESOLUTION_QQVGA_WIDTH		((uint16_t)160)
#define IMAGE_RESOLUTION_QQVGA_HEIGHT		((uint16_t)120)

typedef enum
{
	IMAGE_FORMAT_GRAYSCALE	= 1, /* 1 Byte for each pixel  */
	IMAGE_FORMAT_RGB565		= 2, /* 2 Bytes for each pixel */
	IMAGE_FORMAT_RGB888		= 3, /* 3 Bytes for each pixel */
}IMAGE_Format;

typedef struct
{
	uint8_t *pData;
	uint16_t width;
	uint16_t height;
	IMAGE_Format format;
	uint32_t size;
}IMAGE_HandleTypeDef;

int8_t LIB_IMAGE_InitStruct(IMAGE_HandleTypeDef * img, uint8_t *pImg, uint16_t height, uint16_t width, IMAGE_Format format);

#ifdef __cplusplus
}
#endif

#endif /* INC_LIB_IMAGE_H_ */
