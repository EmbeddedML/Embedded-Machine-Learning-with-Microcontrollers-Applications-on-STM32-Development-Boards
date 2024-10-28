/*
 * lib_slidingwindow.h
 *
 *  Created on: May 29, 2022
 *      Author: Eren Atmaca
 */

#ifndef INC_LIB_SLIDINGWINDOW_H_
#define INC_LIB_SLIDINGWINDOW_H_

#ifdef __cplusplus
extern "C" {
#endif

#include "lib_image.h"

#define OK							((int8_t)0)
#define ERROR						((int8_t)-1)


typedef struct
{
	uint32_t nWidth;
	uint32_t nHeight;
	float currentWidth;
	float currentHeight;
}SW_Params;

typedef struct
{
	IMAGE_HandleTypeDef *input_image;
	IMAGE_HandleTypeDef *output_image;
	SW_Params params;
}SW_TypeDef;

int8_t LIB_SW_Init(SW_TypeDef * sw);
void LIB_SW_SlideWindow(SW_TypeDef * sw, uint8_t percentage);
int8_t LIB_SW_GetWindow(SW_TypeDef * sw);


#ifdef __cplusplus
}
#endif

#endif /* INC_LIB_SLIDINGWINDOW_H_ */
