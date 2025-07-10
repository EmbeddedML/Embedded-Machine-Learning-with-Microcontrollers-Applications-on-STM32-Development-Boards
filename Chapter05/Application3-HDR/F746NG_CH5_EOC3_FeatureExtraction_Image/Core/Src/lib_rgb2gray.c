/*
 * lib_rgb2gray.c
 *
 *  Created on: 9 Apr 2024
 *      Author: Eren Atmaca
 */
#include "lib_rgb2gray.h"

void LIB_RGB2GRAY_Convert565(IMAGE_HandleTypeDef *pImgSrc, IMAGE_HandleTypeDef *pImgDest)
{
	uint8_t r8, g8, b8;
	uint32_t i = 0;
	for (i = 0; i < pImgSrc->size; i=i+2)
	{
		//r8 = pImgSrc->pData[i] & 0xF8;
		//g8 = (((pImgSrc->pData[i] & 0x07) << 3) | ((pImgSrc->pData[i+1] >> 5) & 0x07)) << 2;
		//b8 = (pImgSrc->pData[i+1] & 0x1F) << 3;
		r8 = (pImgSrc->pData[i + 1] & 0xF8) << 3;
		g8 = (((pImgSrc->pData[i + 1] & 0x07) << 5) | ((pImgSrc->pData[i] & 0xE0) >> 3));
		b8 = (pImgSrc->pData[i] & 0x1F) << 3;
		pImgDest->pData[i/2] = (uint8_t)((77 * r8 + 150 * g8 +  29 * b8) >> 8);
	}
}

