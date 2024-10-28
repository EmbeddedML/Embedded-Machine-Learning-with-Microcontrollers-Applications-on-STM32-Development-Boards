################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (9-2020-q2-update)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Drivers/BSP/Components/wm8994/wm8994.c 

C_DEPS += \
./Drivers/BSP/Components/wm8994/wm8994.d 

OBJS += \
./Drivers/BSP/Components/wm8994/wm8994.o 


# Each subdirectory must supply rules for building sources it contributes
Drivers/BSP/Components/wm8994/%.o: ../Drivers/BSP/Components/wm8994/%.c Drivers/BSP/Components/wm8994/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m7 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F746xx -DTF_LITE_STATIC_MEMORY -DARM_MATH_CM7 -c -I../Core/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F7xx/Include -I../Drivers/CMSIS/Include -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH14_EOC1_KeywordSpotting/Include/dsp" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH14_EOC1_KeywordSpotting/PrivateInclude" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH14_EOC1_KeywordSpotting/Include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH14_EOC1_KeywordSpotting/third_party/flatbuffers/include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH14_EOC1_KeywordSpotting" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH14_EOC1_KeywordSpotting/third_party/kissfft" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH14_EOC1_KeywordSpotting/third_party/gemmlowp" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH14_EOC1_KeywordSpotting/third_party/ruy" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Drivers-2f-BSP-2f-Components-2f-wm8994

clean-Drivers-2f-BSP-2f-Components-2f-wm8994:
	-$(RM) ./Drivers/BSP/Components/wm8994/wm8994.d ./Drivers/BSP/Components/wm8994/wm8994.o

.PHONY: clean-Drivers-2f-BSP-2f-Components-2f-wm8994

