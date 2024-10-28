/*
 * lib_rgb2gray.h
 *
 *  Created on: 9 Apr 2024
 *      Author: Eren Atmaca
 */

#ifndef INC_LIB_RGB2GRAY_H_
#define INC_LIB_RGB2GRAY_H_

#ifdef __cplusplus
extern "C" {
#endif

#include "lib_image.h"

void LIB_RGB2GRAY_Convert565(IMAGE_HandleTypeDef *pImgSrc, IMAGE_HandleTypeDef *pImgDest);




#ifdef __cplusplus
}
#endif

#endif /* INC_LIB_RGB2GRAY_H_ */
