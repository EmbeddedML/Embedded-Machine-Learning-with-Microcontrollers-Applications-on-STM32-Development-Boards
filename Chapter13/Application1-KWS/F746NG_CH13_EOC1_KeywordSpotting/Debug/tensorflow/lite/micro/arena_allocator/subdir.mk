################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (9-2020-q2-update)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CC_SRCS += \
../tensorflow/lite/micro/arena_allocator/non_persistent_arena_buffer_allocator.cc \
../tensorflow/lite/micro/arena_allocator/persistent_arena_buffer_allocator.cc \
../tensorflow/lite/micro/arena_allocator/recording_single_arena_buffer_allocator.cc \
../tensorflow/lite/micro/arena_allocator/single_arena_buffer_allocator.cc 

CC_DEPS += \
./tensorflow/lite/micro/arena_allocator/non_persistent_arena_buffer_allocator.d \
./tensorflow/lite/micro/arena_allocator/persistent_arena_buffer_allocator.d \
./tensorflow/lite/micro/arena_allocator/recording_single_arena_buffer_allocator.d \
./tensorflow/lite/micro/arena_allocator/single_arena_buffer_allocator.d 

OBJS += \
./tensorflow/lite/micro/arena_allocator/non_persistent_arena_buffer_allocator.o \
./tensorflow/lite/micro/arena_allocator/persistent_arena_buffer_allocator.o \
./tensorflow/lite/micro/arena_allocator/recording_single_arena_buffer_allocator.o \
./tensorflow/lite/micro/arena_allocator/single_arena_buffer_allocator.o 


# Each subdirectory must supply rules for building sources it contributes
tensorflow/lite/micro/arena_allocator/%.o: ../tensorflow/lite/micro/arena_allocator/%.cc tensorflow/lite/micro/arena_allocator/subdir.mk
	arm-none-eabi-g++ "$<" -mcpu=cortex-m7 -std=gnu++14 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F746xx -DTF_LITE_STATIC_MEMORY -DARM_MATH_CM7 -c -I../Core/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F7xx/Include -I../Drivers/CMSIS/Include -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC1_KeywordSpotting/Include/dsp" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC1_KeywordSpotting/PrivateInclude" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC1_KeywordSpotting/Include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC1_KeywordSpotting" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC1_KeywordSpotting/third_party/flatbuffers/include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC1_KeywordSpotting/third_party/gemmlowp" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC1_KeywordSpotting/third_party/kissfft" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH13_EOC1_KeywordSpotting/third_party/ruy" -O0 -ffunction-sections -fdata-sections -fno-exceptions -fno-rtti -fno-use-cxa-atexit -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-tensorflow-2f-lite-2f-micro-2f-arena_allocator

clean-tensorflow-2f-lite-2f-micro-2f-arena_allocator:
	-$(RM) ./tensorflow/lite/micro/arena_allocator/non_persistent_arena_buffer_allocator.d ./tensorflow/lite/micro/arena_allocator/non_persistent_arena_buffer_allocator.o ./tensorflow/lite/micro/arena_allocator/persistent_arena_buffer_allocator.d ./tensorflow/lite/micro/arena_allocator/persistent_arena_buffer_allocator.o ./tensorflow/lite/micro/arena_allocator/recording_single_arena_buffer_allocator.d ./tensorflow/lite/micro/arena_allocator/recording_single_arena_buffer_allocator.o ./tensorflow/lite/micro/arena_allocator/single_arena_buffer_allocator.d ./tensorflow/lite/micro/arena_allocator/single_arena_buffer_allocator.o

.PHONY: clean-tensorflow-2f-lite-2f-micro-2f-arena_allocator

