################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (9-2020-q2-update)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CC_SRCS += \
../tensorflow/lite/kernels/internal/reference/comparisons.cc \
../tensorflow/lite/kernels/internal/reference/portable_tensor_utils.cc 

CC_DEPS += \
./tensorflow/lite/kernels/internal/reference/comparisons.d \
./tensorflow/lite/kernels/internal/reference/portable_tensor_utils.d 

OBJS += \
./tensorflow/lite/kernels/internal/reference/comparisons.o \
./tensorflow/lite/kernels/internal/reference/portable_tensor_utils.o 


# Each subdirectory must supply rules for building sources it contributes
tensorflow/lite/kernels/internal/reference/%.o: ../tensorflow/lite/kernels/internal/reference/%.cc tensorflow/lite/kernels/internal/reference/subdir.mk
	arm-none-eabi-g++ "$<" -mcpu=cortex-m7 -std=gnu++14 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F746xx -DTF_LITE_STATIC_MEMORY -DARM_MATH_CM7 -c -I../Core/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F7xx/Include -I../Drivers/CMSIS/Include -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC1_HumanActivityRecognition/Include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC1_HumanActivityRecognition/PrivateInclude" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC1_HumanActivityRecognition" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC1_HumanActivityRecognition/third_party/flatbuffers/include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC1_HumanActivityRecognition/third_party/kissfft" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC1_HumanActivityRecognition/third_party/ruy" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC1_HumanActivityRecognition/third_party/gemmlowp" -O0 -ffunction-sections -fdata-sections -fno-exceptions -fno-rtti -fno-use-cxa-atexit -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-tensorflow-2f-lite-2f-kernels-2f-internal-2f-reference

clean-tensorflow-2f-lite-2f-kernels-2f-internal-2f-reference:
	-$(RM) ./tensorflow/lite/kernels/internal/reference/comparisons.d ./tensorflow/lite/kernels/internal/reference/comparisons.o ./tensorflow/lite/kernels/internal/reference/portable_tensor_utils.d ./tensorflow/lite/kernels/internal/reference/portable_tensor_utils.o

.PHONY: clean-tensorflow-2f-lite-2f-kernels-2f-internal-2f-reference

