import numpy as np
import serial
import msvcrt

# Data Type
dType = {1: "TYPE_U8", 2:"TYPE_S8", 3:"TYPE_U16", 
            4:"TYPE_S16", 5: "TYPE_U32", 6:"TYPE_S32", 7:"TYPE_F32"}

MCU_WRITES = 87
MCU_READS  = 82
# Request Type
rqType = { MCU_WRITES: "MCU Write", MCU_READS: "MCU Read"} 

# Init Com Port
def SERIAL_Init(port):
    global __serial    
    __serial = serial.Serial(port, 2000000, timeout = 1)
    __serial.flush()
    print(__serial.name, "Opened")
    print("")

# Wait for MCU Request 
def SERIAL_PollForRequest():
    global requestType
    global dataType
    global byteLength
    while(1):
        if msvcrt.kbhit() and msvcrt.getch() == chr(27).encode():
            print("Exit program!")
            exit(0)
        if np.frombuffer(__serial.read(1), dtype= np.uint8) == 83:
            if np.frombuffer(__serial.read(1), dtype= np.uint8) == 84:
                requestType  = np.frombuffer(__serial.read(1), dtype= np.uint8)
                dataType     = np.frombuffer(__serial.read(1), dtype= np.uint8)
                byteLength   = np.frombuffer(__serial.read(4), dtype= np.uint32)
                dataSize   = byteLength/np.dtype(SERIAL_GetDType(dataType)).itemsize
                
                print("Request Type : ", rqType[int(requestType)])
                print("Data Type    : ", dType[int(dataType)])
                print("Byte Length  : ", int(byteLength), "Bytes")
                print("Data Size    : ", int(dataSize), "Data")
                
                return [int(requestType), int(dataSize), int(dataType)]

# Read MCU Data 
def SERIAL_Read():
    __type = SERIAL_GetDType(dataType)
    data = np.frombuffer(__serial.read(int(byteLength)), dtype = __type)
    print(data)
    print()
    return data

# Get np.dtype from MCU 
def SERIAL_GetDType(__dataType : int):
    __type = int(__dataType)
    if __type ==  1:
        __type = np.uint8
    elif __type ==  2:
        __type = np.int8
    elif __type ==  3:
        __type = np.uint16
    elif __type ==  4:
        __type = np.int16
    elif __type ==  5:
        __type = np.uint32
    elif __type ==  6:
        __type = np.int32  
    elif __type ==  7:
        __type = np.float32 
    return __type

# Writes data to MCU  
def SERIAL_Write(data : np.array):
    print(data)
    print()
    data = data.tobytes()
    __serial.write(data)