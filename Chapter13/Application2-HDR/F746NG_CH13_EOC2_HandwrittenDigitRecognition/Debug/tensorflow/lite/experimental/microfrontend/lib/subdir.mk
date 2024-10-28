################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (9-2020-q2-update)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CC_SRCS += \
../tensorflow/lite/experimental/microfrontend/lib/fft.cc \
../tensorflow/lite/experimental/microfrontend/lib/fft_util.cc \
../tensorflow/lite/experimental/microfrontend/lib/kiss_fft_int16.cc 

C_SRCS += \
../tensorflow/lite/experimental/microfrontend/lib/filterbank.c \
../tensorflow/lite/experimental/microfrontend/lib/filterbank_util.c \
../tensorflow/lite/experimental/microfrontend/lib/frontend.c \
../tensorflow/lite/experimental/microfrontend/lib/frontend_util.c \
../tensorflow/lite/experimental/microfrontend/lib/log_lut.c \
../tensorflow/lite/experimental/microfrontend/lib/log_scale.c \
../tensorflow/lite/experimental/microfrontend/lib/log_scale_util.c \
../tensorflow/lite/experimental/microfrontend/lib/noise_reduction.c \
../tensorflow/lite/experimental/microfrontend/lib/noise_reduction_util.c \
../tensorflow/lite/experimental/microfrontend/lib/pcan_gain_control.c \
../tensorflow/lite/experimental/microfrontend/lib/pcan_gain_control_util.c \
../tensorflow/lite/experimental/microfrontend/lib/window.c \
../tensorflow/lite/experimental/microfrontend/lib/window_util.c 

C_DEPS += \
./tensorflow/lite/experimental/microfrontend/lib/filterbank.d \
./tensorflow/lite/experimental/microfrontend/lib/filterbank_util.d \
./tensorflow/lite/experimental/microfrontend/lib/frontend.d \
./tensorflow/lite/experimental/microfrontend/lib/frontend_util.d \
./tensorflow/lite/experimental/microfrontend/lib/log_lut.d \
./tensorflow/lite/experimental/microfrontend/lib/log_scale.d \
./tensorflow/lite/experimental/microfrontend/lib/log_scale_util.d \
./tensorflow/lite/experimental/microfrontend/lib/noise_reduction.d \
./tensorflow/lite/experimental/microfrontend/lib/noise_reduction_util.d \
./tensorflow/lite/experimental/microfrontend/lib/pcan_gain_control.d \
./tensorflow/lite/experimental/microfrontend/lib/pcan_gain_control_util.d \
./tensorflow/lite/experimental/microfrontend/lib/window.d \
./tensorflow/lite/experimental/microfrontend/lib/window_util.d 

CC_DEPS += \
./tensorflow/lite/experimental/microfrontend/lib/fft.d \
./tensorflow/lite/experimental/microfrontend/lib/fft_util.d \
./tensorflow/lite/experimental/microfrontend/lib/kiss_fft_int16.d 

OBJS += \
./tensorflow/lite/experimental/microfrontend/lib/fft.o \
./tensorflow/lite/experimental/microfrontend/lib/fft_util.o \
./tensorflow/lite/experimental/microfrontend/lib/filterbank.o \
./tensorflow/lite/experimental/microfrontend/lib/filterbank_util.o \
./tensorflow/lite/experimental/microfrontend/lib/frontend.o \
./tensorflow/lite/experimental/microfrontend/lib/frontend_util.o \
./tensorflow/lite/experimental/microfrontend/lib/kiss_fft_int16.o \
./tensorflow/lite/experimental/microfrontend/lib/log_lut.o \
./tensorflow/lite/experimental/microfrontend/lib/log_scale.o \
./tensorflow/lite/experimental/microfrontend/lib/log_scale_util.o \
./tensorflow/lite/experimental/microfrontend/lib/noise_reduction.o \
./tensorflow/lite/experimental/microfrontend/lib/noise_reduction_util.o \
./tensorflow/lite/experimental/microfrontend/lib/pcan_gain_control.o \
./tensorflow/lite/experimental/microfrontend/lib/pcan_gain_control_util.o \
./tensorflow/lite/experimental/microfrontend/lib/window.o \
./tensorflow/lite/experimental/microfrontend/lib/window_util.o 


# Each subdirectory must supply rules for building sources it contributes
tensorflow/lite/experimental/microfrontend/lib/%.o: ../tensorflow/lite/experimental/microfrontend/lib/%.cc tensorflow/lite/experimental/microfrontend/lib/subdir.mk
	arm-none-eabi-g++ "$<" -mcpu=cortex-m7 -std=gnu++14 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F746xx -DARM_MATH_CM7 -DTF_LITE_STATIC_MEMORY -c -I../Core/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F7xx/Include -I../Drivers/CMSIS/Include -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC2_HandwrittenDigitRecognition" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC2_HandwrittenDigitRecognition/third_party/gemmlowp" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC2_HandwrittenDigitRecognition/third_party/flatbuffers/include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC2_HandwrittenDigitRecognition/third_party/kissfft" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC2_HandwrittenDigitRecognition/Include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC2_HandwrittenDigitRecognition/third_party/ruy" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC2_HandwrittenDigitRecognition/Include/dsp" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC2_HandwrittenDigitRecognition/PrivateInclude" -O0 -ffunction-sections -fdata-sections -fno-exceptions -fno-rtti -fno-use-cxa-atexit -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -o "$@"
tensorflow/lite/experimental/microfrontend/lib/%.o: ../tensorflow/lite/experimental/microfrontend/lib/%.c tensorflow/lite/experimental/microfrontend/lib/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m7 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F746xx -DARM_MATH_CM7 -DTF_LITE_STATIC_MEMORY -c -I../Core/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F7xx/Include -I../Drivers/CMSIS/Include -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC2_HandwrittenDigitRecognition" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC2_HandwrittenDigitRecognition/third_party/flatbuffers/include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC2_HandwrittenDigitRecognition/third_party/gemmlowp" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC2_HandwrittenDigitRecognition/third_party/kissfft" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC2_HandwrittenDigitRecognition/third_party/ruy" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC2_HandwrittenDigitRecognition/Include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC2_HandwrittenDigitRecognition/Include/dsp" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC2_HandwrittenDigitRecognition/PrivateInclude" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-tensorflow-2f-lite-2f-experimental-2f-microfrontend-2f-lib

clean-tensorflow-2f-lite-2f-experimental-2f-microfrontend-2f-lib:
	-$(RM) ./tensorflow/lite/experimental/microfrontend/lib/fft.d ./tensorflow/lite/experimental/microfrontend/lib/fft.o ./tensorflow/lite/experimental/microfrontend/lib/fft_util.d ./tensorflow/lite/experimental/microfrontend/lib/fft_util.o ./tensorflow/lite/experimental/microfrontend/lib/filterbank.d ./tensorflow/lite/experimental/microfrontend/lib/filterbank.o ./tensorflow/lite/experimental/microfrontend/lib/filterbank_util.d ./tensorflow/lite/experimental/microfrontend/lib/filterbank_util.o ./tensorflow/lite/experimental/microfrontend/lib/frontend.d ./tensorflow/lite/experimental/microfrontend/lib/frontend.o ./tensorflow/lite/experimental/microfrontend/lib/frontend_util.d ./tensorflow/lite/experimental/microfrontend/lib/frontend_util.o ./tensorflow/lite/experimental/microfrontend/lib/kiss_fft_int16.d ./tensorflow/lite/experimental/microfrontend/lib/kiss_fft_int16.o ./tensorflow/lite/experimental/microfrontend/lib/log_lut.d ./tensorflow/lite/experimental/microfrontend/lib/log_lut.o ./tensorflow/lite/experimental/microfrontend/lib/log_scale.d ./tensorflow/lite/experimental/microfrontend/lib/log_scale.o ./tensorflow/lite/experimental/microfrontend/lib/log_scale_util.d ./tensorflow/lite/experimental/microfrontend/lib/log_scale_util.o ./tensorflow/lite/experimental/microfrontend/lib/noise_reduction.d ./tensorflow/lite/experimental/microfrontend/lib/noise_reduction.o ./tensorflow/lite/experimental/microfrontend/lib/noise_reduction_util.d ./tensorflow/lite/experimental/microfrontend/lib/noise_reduction_util.o ./tensorflow/lite/experimental/microfrontend/lib/pcan_gain_control.d ./tensorflow/lite/experimental/microfrontend/lib/pcan_gain_control.o ./tensorflow/lite/experimental/microfrontend/lib/pcan_gain_control_util.d ./tensorflow/lite/experimental/microfrontend/lib/pcan_gain_control_util.o ./tensorflow/lite/experimental/microfrontend/lib/window.d ./tensorflow/lite/experimental/microfrontend/lib/window.o ./tensorflow/lite/experimental/microfrontend/lib/window_util.d ./tensorflow/lite/experimental/microfrontend/lib/window_util.o

.PHONY: clean-tensorflow-2f-lite-2f-experimental-2f-microfrontend-2f-lib

