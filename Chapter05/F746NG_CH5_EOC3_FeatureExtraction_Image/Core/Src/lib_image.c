/*
 * lib_image.c
 *
 *  Created on: 29 Jan 2023
 *      Author: Eren Atmaca
 */

#include "lib_image.h"

#define __LIB_IMAGE_CHECK_PARAM(param)				{if(param == 0) return IMAGE_ERROR;}

/**
  * @brief Initialize the image structure with required information
  * @param img     Pointer to image structure
  * @param pImg    Pointer to image buffer
  * @param height  height of the image
  * @param width   width of the image
  * @param format  Choose IMAGE_FORMAT_GRAYSCALE, IMAGE_FORMAT_RGB565, or IMAGE_FORMAT_RGB888
  * @retval 0 if successfully initialized
  */
int8_t LIB_IMAGE_InitStruct(IMAGE_HandleTypeDef * img, uint8_t *pImg, uint16_t height, uint16_t width, IMAGE_Format format)
{
	__LIB_IMAGE_CHECK_PARAM(img);
	__LIB_IMAGE_CHECK_PARAM(pImg);
	__LIB_IMAGE_CHECK_PARAM(format);
	__LIB_IMAGE_CHECK_PARAM(width);
	__LIB_IMAGE_CHECK_PARAM(height);
	img->format = format;
	img->height = height;
	img->width 	= width;
	img->pData 	= pImg;
	img->size 	= (uint32_t)img->format * (uint32_t)img->height * (uint32_t)img->width;
	return IMAGE_OK;
}
