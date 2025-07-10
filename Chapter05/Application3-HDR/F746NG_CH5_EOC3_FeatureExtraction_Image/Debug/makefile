################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (9-2020-q2-update)
################################################################################

-include ../makefile.init

RM := rm -rf

# All of the sources participating in the build are defined here
-include sources.mk
-include Drivers/STM32F7xx_HAL_Driver/Src/subdir.mk
-include Drivers/BSP/STM32746G-Discovery/subdir.mk
-include Core/Startup/subdir.mk
-include Core/Src/subdir.mk
-include objects.mk

ifneq ($(MAKECMDGOALS),clean)
ifneq ($(strip $(S_DEPS)),)
-include $(S_DEPS)
endif
ifneq ($(strip $(S_UPPER_DEPS)),)
-include $(S_UPPER_DEPS)
endif
ifneq ($(strip $(C_DEPS)),)
-include $(C_DEPS)
endif
endif

-include ../makefile.defs

OPTIONAL_TOOL_DEPS := \
$(wildcard ../makefile.defs) \
$(wildcard ../makefile.init) \
$(wildcard ../makefile.targets) \


BUILD_ARTIFACT_NAME := F746NG_CH5_EOC3_FeatureExtraction_Image
BUILD_ARTIFACT_EXTENSION := elf
BUILD_ARTIFACT_PREFIX :=
BUILD_ARTIFACT := $(BUILD_ARTIFACT_PREFIX)$(BUILD_ARTIFACT_NAME)$(if $(BUILD_ARTIFACT_EXTENSION),.$(BUILD_ARTIFACT_EXTENSION),)

# Add inputs and outputs from these tool invocations to the build variables 
EXECUTABLES += \
F746NG_CH5_EOC3_FeatureExtraction_Image.elf \

SIZE_OUTPUT += \
default.size.stdout \

OBJDUMP_LIST += \
F746NG_CH5_EOC3_FeatureExtraction_Image.list \

OBJCOPY_BIN += \
F746NG_CH5_EOC3_FeatureExtraction_Image.bin \


# All Target
all: main-build

# Main-build Target
main-build: F746NG_CH5_EOC3_FeatureExtraction_Image.elf secondary-outputs

# Tool invocations
F746NG_CH5_EOC3_FeatureExtraction_Image.elf: $(OBJS) $(USER_OBJS) D:\Workspaces\STM32MLBookEOCWorkspace\F746NG_CH5_EOC3_FeatureExtraction_Image\STM32F746NGHX_FLASH.ld makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-gcc -o "F746NG_CH5_EOC3_FeatureExtraction_Image.elf" @"objects.list" $(USER_OBJS) $(LIBS) -mcpu=cortex-m7 -T"D:\Workspaces\STM32MLBookEOCWorkspace\F746NG_CH5_EOC3_FeatureExtraction_Image\STM32F746NGHX_FLASH.ld" --specs=nosys.specs -Wl,-Map="F746NG_CH5_EOC3_FeatureExtraction_Image.map" -Wl,--gc-sections -static --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -Wl,--start-group -lc -lm -Wl,--end-group
	@echo 'Finished building target: $@'
	@echo ' '

default.size.stdout: $(EXECUTABLES) makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-size  $(EXECUTABLES)
	@echo 'Finished building: $@'
	@echo ' '

F746NG_CH5_EOC3_FeatureExtraction_Image.list: $(EXECUTABLES) makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-objdump -h -S $(EXECUTABLES) > "F746NG_CH5_EOC3_FeatureExtraction_Image.list"
	@echo 'Finished building: $@'
	@echo ' '

F746NG_CH5_EOC3_FeatureExtraction_Image.bin: $(EXECUTABLES) makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-objcopy  -O binary $(EXECUTABLES) "F746NG_CH5_EOC3_FeatureExtraction_Image.bin"
	@echo 'Finished building: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) F746NG_CH5_EOC3_FeatureExtraction_Image.bin F746NG_CH5_EOC3_FeatureExtraction_Image.elf F746NG_CH5_EOC3_FeatureExtraction_Image.list default.size.stdout
	-@echo ' '

secondary-outputs: $(SIZE_OUTPUT) $(OBJDUMP_LIST) $(OBJCOPY_BIN)

fail-specified-linker-script-missing:
	@echo 'Error: Cannot find the specified linker script. Check the linker settings in the build configuration.'
	@exit 2

warn-no-linker-script-specified:
	@echo 'Warning: No linker script specified. Check the linker settings in the build configuration.'

.PHONY: all clean dependents main-build fail-specified-linker-script-missing warn-no-linker-script-specified

-include ../makefile.targets
