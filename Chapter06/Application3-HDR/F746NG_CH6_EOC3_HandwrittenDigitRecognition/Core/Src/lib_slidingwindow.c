/*
 * sliding_window.c
 *
 *  Created on: May 29, 2022
 *      Author: Eren Atmaca
 */


#include <lib_slidingwindow.h>

#define IS_PARAM_IN_INTERVAL(prm) 	(((prm) >= 20) && ((prm) <= 800))
#define IS_FORMAT_VALID(format) 	(((format) == IMAGE_FORMAT_GRAYSCALE) || \
											((format) == IMAGE_FORMAT_RGB565) || \
											((format) == IMAGE_FORMAT_RGB888))
#define IS_PARAM_NON_ZERO(prm) 		((prm) != 0)

int8_t LIB_SW_Init(SW_TypeDef * sw)
{
	if(IS_PARAM_IN_INTERVAL(sw->input_image->height) &&
			IS_PARAM_IN_INTERVAL(sw->input_image->width) &&
			IS_PARAM_IN_INTERVAL(sw->output_image->height) &&
			IS_PARAM_IN_INTERVAL(sw->output_image->width) &&
			IS_FORMAT_VALID(sw->input_image->format))
	{
		sw->params.nHeight 	= sw->input_image->height / sw->output_image->height;
		sw->params.nWidth 	= sw->input_image->width  / sw->output_image->width;
		sw->params.currentHeight 	= 0;
		sw->params.currentWidth		= 0;

		return OK;
	}
	return ERROR;
}

void LIB_SW_SlideWindow(SW_TypeDef * sw, uint8_t percentage)
{
	float slide;
	if (percentage <= 0 || percentage > 100)
	{
		percentage = 100;
	}
	slide = (float) percentage/100;
	sw->params.currentWidth		= sw->params.currentWidth  + slide;
	if (sw->params.currentWidth >= sw->params.nWidth)
	{
		sw->params.currentHeight = sw->params.currentHeight + slide;
		sw->params.currentWidth = 0;
	}
	if (sw->params.currentHeight >= sw->params.nHeight)
	{
		sw->params.currentHeight = 0;
	}

}

int8_t LIB_SW_GetWindow(SW_TypeDef * sw)
{
	if(!(IS_PARAM_NON_ZERO(sw->input_image->pData) && IS_PARAM_NON_ZERO(sw->output_image->pData)))
	{
		return ERROR;
	}
	float heightIndexf = sw->params.currentHeight * sw->input_image->width  * sw->input_image->format * sw->output_image->height;
	float widthIndexf  = sw->params.currentWidth  * sw->output_image->width * sw->input_image->format;
	uint32_t heightIndex = heightIndexf;
	uint32_t widthIndex  = widthIndexf;
	uint32_t x = 0;
	for (uint32_t i = 0;i < sw->output_image->height; i++)
	{
		for (uint32_t j = 0; j < sw->output_image->width * sw->input_image->format; j++)
		{
			sw->output_image->pData[x] = sw->input_image->pData[(j + widthIndex) +  (heightIndex + (i * sw->input_image->width * sw->input_image->format)) ];
			x++;
		}
	}
	return OK;
}
