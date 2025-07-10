
# Chapter 4 - DATA ACQUISITION FROM SENSORS

## About This Chapter

Machine learning methods depend on data. Therefore, the first step for a machine learning system is data acquisition from sensors. We consider this operation in this chapter. To do so, we divide the operation into five parts: First, we handle data transfer between the PC and STM32 microcontroller. The aim here is twofold. When we transfer data from the microcontroller to PC, we can analyze and display it in detail there. When we transfer data from the PC to microcontroller, we can perform controlled experiments for our machine learning system running on the microcontroller. Second, we evaluate data acquisition from the relative humidity and temperature sensor. Third, we cover data acquisition from the accelerometer, gyroscope, and magnetometer sensor. Fourth, we introduce audio signal acquisition. Fifth, we focus on the B-CAMS-OMV camera module and explore acquiring digital images from it. In all these operations, we follow the same strategy as hardware setup, data acquisition and transfer at the microcontroller side, and data transfer at the PC side. Hence, the reader can form a complete setup to acquire and transfer data between the microcontroller and PC. Moreover, we cover all the mentioned topics from the STM32CubeIDE and Mbed Studio perspectives. Hence, the reader can select the appropriate platform to perform all the mentioned operations.

## Listings
<center>

| Description                      | Code                                                                   |
| -------------------------------- | ---------------------------------------------------------------------- |
| GPIO                             | [![Code](../Images/stm32.png)](CubeIDEProjects/F746NG_GPIO)            |
| EXTI                             | [![Code](../Images/stm32.png)](CubeIDEProjects/F746NG_EXTI)            |
| Timer Interrupt                  | [![Code](../Images/stm32.png)](CubeIDEProjects/F746NG_TIMER_INTERRUPT) |
| Data Transfer from PC to board   | [![Code](../Images/stm32.png)](CubeIDEProjects/F746NG_SERIAL_PC2STM)   |
| Data Transfer from Board to PC   | [![Code](../Images/stm32.png)](CubeIDEProjects/F746NG_SERIAL_STM2PC)   |
| Two-way Serial Data Transfer     | [![Code](../Images/stm32.png)](CubeIDEProjects/F746NG_SERIAL)          |
| Image Transfer from PC to board  | [![Code](../Images/stm32.png)](CubeIDEProjects/F746NG_PC2STM_IMG)      |
| Data Acquisition from BNO055     | [![Code](../Images/stm32.png)](CubeIDEProjects/F746NG_BNO055)          |
| Data Acquisition from Microphone | [![Code](../Images/stm32.png)](CubeIDEProjects/F746NG_AUDIO)           |
| Data Acquisition from HTS221     | [![Code](../Images/stm32.png)](CubeIDEProjects/F746NG_HTS221)          |
| Data Acquisition from OV5640     | [![Code](../Images/stm32.png)](CubeIDEProjects/F746NG_OV5640)          |

</center>

             
    
               
           
