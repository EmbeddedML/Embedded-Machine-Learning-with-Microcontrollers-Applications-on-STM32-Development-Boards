################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (9-2020-q2-update)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CC_SRCS += \
../Core/Src/mlp_fsdd_model.cc 

C_SRCS += \
../Core/Src/ks_feature_extraction.c \
../Core/Src/lib_audio.c \
../Core/Src/lib_serial.c \
../Core/Src/stm32f7xx_hal_msp.c \
../Core/Src/stm32f7xx_it.c \
../Core/Src/syscalls.c \
../Core/Src/sysmem.c \
../Core/Src/system_stm32f7xx.c 

CPP_SRCS += \
../Core/Src/lib_model.cpp \
../Core/Src/main.cpp 

C_DEPS += \
./Core/Src/ks_feature_extraction.d \
./Core/Src/lib_audio.d \
./Core/Src/lib_serial.d \
./Core/Src/stm32f7xx_hal_msp.d \
./Core/Src/stm32f7xx_it.d \
./Core/Src/syscalls.d \
./Core/Src/sysmem.d \
./Core/Src/system_stm32f7xx.d 

CC_DEPS += \
./Core/Src/mlp_fsdd_model.d 

OBJS += \
./Core/Src/ks_feature_extraction.o \
./Core/Src/lib_audio.o \
./Core/Src/lib_model.o \
./Core/Src/lib_serial.o \
./Core/Src/main.o \
./Core/Src/mlp_fsdd_model.o \
./Core/Src/stm32f7xx_hal_msp.o \
./Core/Src/stm32f7xx_it.o \
./Core/Src/syscalls.o \
./Core/Src/sysmem.o \
./Core/Src/system_stm32f7xx.o 

CPP_DEPS += \
./Core/Src/lib_model.d \
./Core/Src/main.d 


# Each subdirectory must supply rules for building sources it contributes
Core/Src/%.o: ../Core/Src/%.c Core/Src/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m7 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F746xx -DTF_LITE_STATIC_MEMORY -DARM_MATH_CM7 -c -I../Core/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F7xx/Include -I../Drivers/CMSIS/Include -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/Include/dsp" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/Include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/PrivateInclude" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/third_party/flatbuffers/include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/third_party/gemmlowp" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/third_party/kissfft" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/third_party/ruy" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting" -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -o "$@"
Core/Src/%.o: ../Core/Src/%.cpp Core/Src/subdir.mk
	arm-none-eabi-g++ "$<" -mcpu=cortex-m7 -std=gnu++14 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F746xx -DTF_LITE_STATIC_MEMORY -DARM_MATH_CM7 -c -I../Core/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F7xx/Include -I../Drivers/CMSIS/Include -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/Include/dsp" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/Include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/PrivateInclude" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/third_party/flatbuffers/include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/third_party/gemmlowp" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/third_party/kissfft" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/third_party/ruy" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting" -O0 -ffunction-sections -fdata-sections -fno-exceptions -fno-rtti -fno-use-cxa-atexit -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -o "$@"
Core/Src/%.o: ../Core/Src/%.cc Core/Src/subdir.mk
	arm-none-eabi-g++ "$<" -mcpu=cortex-m7 -std=gnu++14 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F746xx -DTF_LITE_STATIC_MEMORY -DARM_MATH_CM7 -c -I../Core/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F7xx/Include -I../Drivers/CMSIS/Include -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/Include/dsp" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/Include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/PrivateInclude" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/third_party/flatbuffers/include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/third_party/gemmlowp" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/third_party/kissfft" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting/third_party/ruy" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC2_KeywordSpotting" -O0 -ffunction-sections -fdata-sections -fno-exceptions -fno-rtti -fno-use-cxa-atexit -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Core-2f-Src

clean-Core-2f-Src:
	-$(RM) ./Core/Src/ks_feature_extraction.d ./Core/Src/ks_feature_extraction.o ./Core/Src/lib_audio.d ./Core/Src/lib_audio.o ./Core/Src/lib_model.d ./Core/Src/lib_model.o ./Core/Src/lib_serial.d ./Core/Src/lib_serial.o ./Core/Src/main.d ./Core/Src/main.o ./Core/Src/mlp_fsdd_model.d ./Core/Src/mlp_fsdd_model.o ./Core/Src/stm32f7xx_hal_msp.d ./Core/Src/stm32f7xx_hal_msp.o ./Core/Src/stm32f7xx_it.d ./Core/Src/stm32f7xx_it.o ./Core/Src/syscalls.d ./Core/Src/syscalls.o ./Core/Src/sysmem.d ./Core/Src/sysmem.o ./Core/Src/system_stm32f7xx.d ./Core/Src/system_stm32f7xx.o

.PHONY: clean-Core-2f-Src

