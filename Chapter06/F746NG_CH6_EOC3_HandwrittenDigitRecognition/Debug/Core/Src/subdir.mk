################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (9-2020-q2-update)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Core/Src/dt_cls_config.c \
../Core/Src/dt_cls_inference.c \
../Core/Src/hdr_feature_extraction.c \
../Core/Src/lib_image.c \
../Core/Src/lib_mpu.c \
../Core/Src/lib_ov5640.c \
../Core/Src/lib_rgb2gray.c \
../Core/Src/lib_serial.c \
../Core/Src/lib_serialimage.c \
../Core/Src/lib_slidingwindow.c \
../Core/Src/main.c \
../Core/Src/ov5640.c \
../Core/Src/ov5640_reg.c \
../Core/Src/stm32f7xx_hal_msp.c \
../Core/Src/stm32f7xx_it.c \
../Core/Src/syscalls.c \
../Core/Src/sysmem.c \
../Core/Src/system_stm32f7xx.c 

OBJS += \
./Core/Src/dt_cls_config.o \
./Core/Src/dt_cls_inference.o \
./Core/Src/hdr_feature_extraction.o \
./Core/Src/lib_image.o \
./Core/Src/lib_mpu.o \
./Core/Src/lib_ov5640.o \
./Core/Src/lib_rgb2gray.o \
./Core/Src/lib_serial.o \
./Core/Src/lib_serialimage.o \
./Core/Src/lib_slidingwindow.o \
./Core/Src/main.o \
./Core/Src/ov5640.o \
./Core/Src/ov5640_reg.o \
./Core/Src/stm32f7xx_hal_msp.o \
./Core/Src/stm32f7xx_it.o \
./Core/Src/syscalls.o \
./Core/Src/sysmem.o \
./Core/Src/system_stm32f7xx.o 

C_DEPS += \
./Core/Src/dt_cls_config.d \
./Core/Src/dt_cls_inference.d \
./Core/Src/hdr_feature_extraction.d \
./Core/Src/lib_image.d \
./Core/Src/lib_mpu.d \
./Core/Src/lib_ov5640.d \
./Core/Src/lib_rgb2gray.d \
./Core/Src/lib_serial.d \
./Core/Src/lib_serialimage.d \
./Core/Src/lib_slidingwindow.d \
./Core/Src/main.d \
./Core/Src/ov5640.d \
./Core/Src/ov5640_reg.d \
./Core/Src/stm32f7xx_hal_msp.d \
./Core/Src/stm32f7xx_it.d \
./Core/Src/syscalls.d \
./Core/Src/sysmem.d \
./Core/Src/system_stm32f7xx.d 


# Each subdirectory must supply rules for building sources it contributes
Core/Src/%.o: ../Core/Src/%.c Core/Src/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m7 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F746xx -c -I../Core/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F7xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Core-2f-Src

clean-Core-2f-Src:
	-$(RM) ./Core/Src/dt_cls_config.d ./Core/Src/dt_cls_config.o ./Core/Src/dt_cls_inference.d ./Core/Src/dt_cls_inference.o ./Core/Src/hdr_feature_extraction.d ./Core/Src/hdr_feature_extraction.o ./Core/Src/lib_image.d ./Core/Src/lib_image.o ./Core/Src/lib_mpu.d ./Core/Src/lib_mpu.o ./Core/Src/lib_ov5640.d ./Core/Src/lib_ov5640.o ./Core/Src/lib_rgb2gray.d ./Core/Src/lib_rgb2gray.o ./Core/Src/lib_serial.d ./Core/Src/lib_serial.o ./Core/Src/lib_serialimage.d ./Core/Src/lib_serialimage.o ./Core/Src/lib_slidingwindow.d ./Core/Src/lib_slidingwindow.o ./Core/Src/main.d ./Core/Src/main.o ./Core/Src/ov5640.d ./Core/Src/ov5640.o ./Core/Src/ov5640_reg.d ./Core/Src/ov5640_reg.o ./Core/Src/stm32f7xx_hal_msp.d ./Core/Src/stm32f7xx_hal_msp.o ./Core/Src/stm32f7xx_it.d ./Core/Src/stm32f7xx_it.o ./Core/Src/syscalls.d ./Core/Src/syscalls.o ./Core/Src/sysmem.d ./Core/Src/sysmem.o ./Core/Src/system_stm32f7xx.d ./Core/Src/system_stm32f7xx.o

.PHONY: clean-Core-2f-Src

