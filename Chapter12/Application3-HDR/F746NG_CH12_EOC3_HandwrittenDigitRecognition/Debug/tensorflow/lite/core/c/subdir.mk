################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (9-2020-q2-update)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CC_SRCS += \
../tensorflow/lite/core/c/common.cc 

CC_DEPS += \
./tensorflow/lite/core/c/common.d 

OBJS += \
./tensorflow/lite/core/c/common.o 


# Each subdirectory must supply rules for building sources it contributes
tensorflow/lite/core/c/%.o: ../tensorflow/lite/core/c/%.cc tensorflow/lite/core/c/subdir.mk
	arm-none-eabi-g++ "$<" -mcpu=cortex-m7 -std=gnu++14 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F746xx -DARM_MATH_CM7 -DTF_LITE_STATIC_MEMORY -c -I../Core/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F7xx/Include -I../Drivers/CMSIS/Include -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC3_HandwrittenDigitRecognition/third_party/flatbuffers/include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC3_HandwrittenDigitRecognition/third_party/gemmlowp" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC3_HandwrittenDigitRecognition/third_party/kissfft" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC3_HandwrittenDigitRecognition/third_party/ruy" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC3_HandwrittenDigitRecognition" -O0 -ffunction-sections -fdata-sections -fno-exceptions -fno-rtti -fno-use-cxa-atexit -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-tensorflow-2f-lite-2f-core-2f-c

clean-tensorflow-2f-lite-2f-core-2f-c:
	-$(RM) ./tensorflow/lite/core/c/common.d ./tensorflow/lite/core/c/common.o

.PHONY: clean-tensorflow-2f-lite-2f-core-2f-c

