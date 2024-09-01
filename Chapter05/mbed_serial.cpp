#include "mbed.h"
#include "lib_rng.h"
#include "lib_serial.h"
#include "lib_uart.h"

int main(){
    LIB_RNG_Init();
    LIB_UART_Init();
    
    while (true){
        uint32_t randomNumber = LIB_RNG_GetRandomNumber();
        LIB_SERIAL_Transmit(&randomNumber, 1, TYPE_U32);
        wait_us(1000000);
    }
}