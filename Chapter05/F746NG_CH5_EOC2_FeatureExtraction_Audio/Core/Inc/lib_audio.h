/*
 * lib_audio.h
 *
 *  Created on: Aug 8, 2023
 *      Author: Eren Atmaca
 */

#ifndef INC_LIB_AUDIO_H_
#define INC_LIB_AUDIO_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdint.h>

int8_t LIB_AUDIO_Init(void);
void LIB_AUDIO_StartRecording(uint16_t *pData, uint32_t length);
int8_t LIB_AUDIO_PollForRecording(uint16_t timeout);
void BSP_AUDIO_IN_TransferComplete_CallBack(void);
void AUDIO_IN_SAIx_DMAx_IRQHandler(void);


#ifdef __cplusplus
}
#endif

#endif /* INC_LIB_AUDIO_H_ */
