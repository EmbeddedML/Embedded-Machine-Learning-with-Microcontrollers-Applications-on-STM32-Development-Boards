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
-include Drivers/BSP/Components/wm8994/subdir.mk
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


BUILD_ARTIFACT_NAME := F746NG_CH6_EOC2_KeywordSpotting
BUILD_ARTIFACT_EXTENSION := elf
BUILD_ARTIFACT_PREFIX :=
BUILD_ARTIFACT := $(BUILD_ARTIFACT_PREFIX)$(BUILD_ARTIFACT_NAME)$(if $(BUILD_ARTIFACT_EXTENSION),.$(BUILD_ARTIFACT_EXTENSION),)

# Add inputs and outputs from these tool invocations to the build variables 
EXECUTABLES += \
F746NG_CH6_EOC2_KeywordSpotting.elf \

SIZE_OUTPUT += \
default.size.stdout \

OBJDUMP_LIST += \
F746NG_CH6_EOC2_KeywordSpotting.list \

OBJCOPY_BIN += \
F746NG_CH6_EOC2_KeywordSpotting.bin \


# All Target
all: main-build

# Main-build Target
main-build: F746NG_CH6_EOC2_KeywordSpotting.elf secondary-outputs

# Tool invocations
F746NG_CH6_EOC2_KeywordSpotting.elf: $(OBJS) $(USER_OBJS) D:\Workspaces\STM32MLBookEOCWorkspace\F746NG_CH6_EOC2_KeywordSpotting\STM32F746NGHX_FLASH.ld makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-gcc -o "F746NG_CH6_EOC2_KeywordSpotting.elf" @"objects.list" $(USER_OBJS) $(LIBS) -mcpu=cortex-m7 -T"D:\Workspaces\STM32MLBookEOCWorkspace\F746NG_CH6_EOC2_KeywordSpotting\STM32F746NGHX_FLASH.ld" --specs=nosys.specs -Wl,-Map="F746NG_CH6_EOC2_KeywordSpotting.map" -Wl,--gc-sections -static -L"D:\Workspaces\STM32MLBookEOCWorkspace\F746NG_CH6_EOC2_KeywordSpotting" --specs=nano.specs -mfpu=fpv5-sp-d16 -mfloat-abi=hard -mthumb -Wl,--start-group -lc -lm -Wl,--end-group
	@echo 'Finished building target: $@'
	@echo ' '

default.size.stdout: $(EXECUTABLES) makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-size  $(EXECUTABLES)
	@echo 'Finished building: $@'
	@echo ' '

F746NG_CH6_EOC2_KeywordSpotting.list: $(EXECUTABLES) makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-objdump -h -S $(EXECUTABLES) > "F746NG_CH6_EOC2_KeywordSpotting.list"
	@echo 'Finished building: $@'
	@echo ' '

F746NG_CH6_EOC2_KeywordSpotting.bin: $(EXECUTABLES) makefile objects.list $(OPTIONAL_TOOL_DEPS)
	arm-none-eabi-objcopy  -O binary $(EXECUTABLES) "F746NG_CH6_EOC2_KeywordSpotting.bin"
	@echo 'Finished building: $@'
	@echo ' '

# Other Targets
clean:
	-$(RM) F746NG_CH6_EOC2_KeywordSpotting.bin F746NG_CH6_EOC2_KeywordSpotting.elf F746NG_CH6_EOC2_KeywordSpotting.list default.size.stdout
	-@echo ' '

secondary-outputs: $(SIZE_OUTPUT) $(OBJDUMP_LIST) $(OBJCOPY_BIN)

fail-specified-linker-script-missing:
	@echo 'Error: Cannot find the specified linker script. Check the linker settings in the build configuration.'
	@exit 2

warn-no-linker-script-specified:
	@echo 'Warning: No linker script specified. Check the linker settings in the build configuration.'

.PHONY: all clean dependents main-build fail-specified-linker-script-missing warn-no-linker-script-specified

-include ../makefile.targets
