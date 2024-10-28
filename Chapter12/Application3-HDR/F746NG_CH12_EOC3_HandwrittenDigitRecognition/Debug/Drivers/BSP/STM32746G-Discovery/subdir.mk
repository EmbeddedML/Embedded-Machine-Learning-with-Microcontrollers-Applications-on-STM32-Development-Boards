################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (9-2020-q2-update)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Drivers/BSP/STM32746G-Discovery/stm32746g_discovery_sdram.c 

C_DEPS += \
./Drivers/BSP/STM32746G-Discovery/stm32746g_discovery_sdram.d 

OBJS += \
./Drivers/BSP/STM32746G-Discovery/stm32746g_discovery_sdram.o 


# Each subdirectory must supply rules for building sources it contributes
Drivers/BSP/STM32746G-Discovery/%.o: ../Drivers/BSP/STM32746G-Discovery/%.c Drivers/BSP/STM32746G-Discovery/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m7 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F746xx -DARM_MATH_CM7 -DTF_LITE_STATIC_MEMORY -c -I../Core/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F7xx/Include -I../Drivers/CMSIS/Include -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC3_HandwrittenDigitRecognition/third_party/flatbuffers/include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC3_HandwrittenDigitRecognition/third_party/gemmlowp" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC3_HandwrittenDigitRecognition/third_party/kissfft" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC3_HandwrittenDigitRecognition/third_party/ruy" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC3_HandwrittenDigitRecognition" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Drivers-2f-BSP-2f-STM32746G-2d-Discovery

clean-Drivers-2f-BSP-2f-STM32746G-2d-Discovery:
	-$(RM) ./Drivers/BSP/STM32746G-Discovery/stm32746g_discovery_sdram.d ./Drivers/BSP/STM32746G-Discovery/stm32746g_discovery_sdram.o

.PHONY: clean-Drivers-2f-BSP-2f-STM32746G-2d-Discovery

