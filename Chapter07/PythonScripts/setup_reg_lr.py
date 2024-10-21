import os
import numpy as np
from sklearn2c import LinearRegressor
import py_serial
from Data.paths import REGRESSION_DATA_DIR
from Models.paths import REGRESSION_MODEL_DIR

py_serial.SERIAL_Init("COM4")

train_samples = np.load(os.path.join(REGRESSION_DATA_DIR, "reg_samples.npy"))
linear = LinearRegressor.load(os.path.join(REGRESSION_MODEL_DIR,"linear_regressor_sine.joblib"))

i = 0
while 1:
    rqType, datalength, dataType = py_serial.SERIAL_PollForRequest()
    
    if rqType == py_serial.MCU_WRITES:
        # INPUT -> FROM MCU TO PC
        inputs = py_serial.SERIAL_Read()
    
    elif rqType == py_serial.MCU_READS:
        # INPUT -> FROM PC TO MCU
        inputs = train_samples[i:i+1].astype(py_serial.SERIAL_GetDType(dataType))
        i = i + 1
        if i >= len(train_samples):
            i = 0
        py_serial.SERIAL_Write(inputs)


    pcout = linear.predict(np.reshape(inputs, (1, datalength)))
    rqType, datalength, dataType = py_serial.SERIAL_PollForRequest()
    if rqType == py_serial.MCU_WRITES:
        mcuout = py_serial.SERIAL_Read()
        print()
        print("Inputs : " + str(inputs))
        print("PC Output : " + str(pcout))
        print("MCU Output : " + str(mcuout))
        print()



