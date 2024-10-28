################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (9-2020-q2-update)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CC_SRCS += \
../tensorflow/lite/micro/debug_log.cc \
../tensorflow/lite/micro/fake_micro_context.cc \
../tensorflow/lite/micro/flatbuffer_utils.cc \
../tensorflow/lite/micro/memory_helpers.cc \
../tensorflow/lite/micro/micro_allocation_info.cc \
../tensorflow/lite/micro/micro_allocator.cc \
../tensorflow/lite/micro/micro_context.cc \
../tensorflow/lite/micro/micro_interpreter.cc \
../tensorflow/lite/micro/micro_interpreter_context.cc \
../tensorflow/lite/micro/micro_interpreter_graph.cc \
../tensorflow/lite/micro/micro_log.cc \
../tensorflow/lite/micro/micro_op_resolver.cc \
../tensorflow/lite/micro/micro_profiler.cc \
../tensorflow/lite/micro/micro_resource_variable.cc \
../tensorflow/lite/micro/micro_time.cc \
../tensorflow/lite/micro/micro_utils.cc \
../tensorflow/lite/micro/mock_micro_graph.cc \
../tensorflow/lite/micro/recording_micro_allocator.cc \
../tensorflow/lite/micro/system_setup.cc \
../tensorflow/lite/micro/test_helper_custom_ops.cc \
../tensorflow/lite/micro/test_helpers.cc 

CC_DEPS += \
./tensorflow/lite/micro/debug_log.d \
./tensorflow/lite/micro/fake_micro_context.d \
./tensorflow/lite/micro/flatbuffer_utils.d \
./tensorflow/lite/micro/memory_helpers.d \
./tensorflow/lite/micro/micro_allocation_info.d \
./tensorflow/lite/micro/micro_allocator.d \
./tensorflow/lite/micro/micro_context.d \
./tensorflow/lite/micro/micro_interpreter.d \
./tensorflow/lite/micro/micro_interpreter_context.d \
./tensorflow/lite/micro/micro_interpreter_graph.d \
./tensorflow/lite/micro/micro_log.d \
./tensorflow/lite/micro/micro_op_resolver.d \
./tensorflow/lite/micro/micro_profiler.d \
./tensorflow/lite/micro/micro_resource_variable.d \
./tensorflow/lite/micro/micro_time.d \
./tensorflow/lite/micro/micro_utils.d \
./tensorflow/lite/micro/mock_micro_graph.d \
./tensorflow/lite/micro/recording_micro_allocator.d \
./tensorflow/lite/micro/system_setup.d \
./tensorflow/lite/micro/test_helper_custom_ops.d \
./tensorflow/lite/micro/test_helpers.d 

OBJS += \
./tensorflow/lite/micro/debug_log.o \
./tensorflow/lite/micro/fake_micro_context.o \
./tensorflow/lite/micro/flatbuffer_utils.o \
./tensorflow/lite/micro/memory_helpers.o \
./tensorflow/lite/micro/micro_allocation_info.o \
./tensorflow/lite/micro/micro_allocator.o \
./tensorflow/lite/micro/micro_context.o \
./tensorflow/lite/micro/micro_interpreter.o \
./tensorflow/lite/micro/micro_interpreter_context.o \
./tensorflow/lite/micro/micro_interpreter_graph.o \
./tensorflow/lite/micro/micro_log.o \
./tensorflow/lite/micro/micro_op_resolver.o \
./tensorflow/lite/micro/micro_profiler.o \
./tensorflow/lite/micro/micro_resource_variable.o \
./tensorflow/lite/micro/micro_time.o \
./tensorflow/lite/micro/micro_utils.o \
./tensorflow/lite/micro/mock_micro_graph.o \
./tensorflow/lite/micro/recording_micro_allocator.o \
./tensorflow/lite/micro/system_setup.o \
./tensorflow/lite/micro/test_helper_custom_ops.o \
./tensorflow/lite/micro/test_helpers.o 


# Each subdirectory must supply rules for building sources it contributes
tensorflow/lite/micro/%.o: ../tensorflow/lite/micro/%.cc tensorflow/lite/micro/subdir.mk
	arm-none-eabi-g++ "$<" -mcpu=cortex-m7 -std=gnu++14 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F746xx -DARM_MATH_CM7 -DTF_LITE_STATIC_MEMORY -c -I../Core/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc -I../Drivers/STM32F7xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F7xx/Include -I../Drivers/CMSIS/Include -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC3_HandwrittenDigitRecognition/third_party/flatbuffers/include" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC3_HandwrittenDigitRecognition/third_party/gemmlowp" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC3_HandwrittenDigitRecognition/third_party/kissfft" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC3_HandwrittenDigitRecognition/third_party/ruy" -I"D:/Workspaces/STM32MLBookEOCWorkspace/F746NG_CH12_EOC3_HandwrittenDigitRecognition" -O0 -ffunction-sections -fdata-sections -fno-exceptions -fno-rtti -fno-use-cxa-atexit -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-tensorflow-2f-lite-2f-micro

clean-tensorflow-2f-lite-2f-micro:
	-$(RM) ./tensorflow/lite/micro/debug_log.d ./tensorflow/lite/micro/debug_log.o ./tensorflow/lite/micro/fake_micro_context.d ./tensorflow/lite/micro/fake_micro_context.o ./tensorflow/lite/micro/flatbuffer_utils.d ./tensorflow/lite/micro/flatbuffer_utils.o ./tensorflow/lite/micro/memory_helpers.d ./tensorflow/lite/micro/memory_helpers.o ./tensorflow/lite/micro/micro_allocation_info.d ./tensorflow/lite/micro/micro_allocation_info.o ./tensorflow/lite/micro/micro_allocator.d ./tensorflow/lite/micro/micro_allocator.o ./tensorflow/lite/micro/micro_context.d ./tensorflow/lite/micro/micro_context.o ./tensorflow/lite/micro/micro_interpreter.d ./tensorflow/lite/micro/micro_interpreter.o ./tensorflow/lite/micro/micro_interpreter_context.d ./tensorflow/lite/micro/micro_interpreter_context.o ./tensorflow/lite/micro/micro_interpreter_graph.d ./tensorflow/lite/micro/micro_interpreter_graph.o ./tensorflow/lite/micro/micro_log.d ./tensorflow/lite/micro/micro_log.o ./tensorflow/lite/micro/micro_op_resolver.d ./tensorflow/lite/micro/micro_op_resolver.o ./tensorflow/lite/micro/micro_profiler.d ./tensorflow/lite/micro/micro_profiler.o ./tensorflow/lite/micro/micro_resource_variable.d ./tensorflow/lite/micro/micro_resource_variable.o ./tensorflow/lite/micro/micro_time.d ./tensorflow/lite/micro/micro_time.o ./tensorflow/lite/micro/micro_utils.d ./tensorflow/lite/micro/micro_utils.o ./tensorflow/lite/micro/mock_micro_graph.d ./tensorflow/lite/micro/mock_micro_graph.o ./tensorflow/lite/micro/recording_micro_allocator.d ./tensorflow/lite/micro/recording_micro_allocator.o ./tensorflow/lite/micro/system_setup.d ./tensorflow/lite/micro/system_setup.o ./tensorflow/lite/micro/test_helper_custom_ops.d ./tensorflow/lite/micro/test_helper_custom_ops.o ./tensorflow/lite/micro/test_helpers.d ./tensorflow/lite/micro/test_helpers.o

.PHONY: clean-tensorflow-2f-lite-2f-micro

