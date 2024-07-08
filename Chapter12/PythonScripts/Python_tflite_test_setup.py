import os.path as osp
import numpy as np
import tensorflow as tf
import py_serial 

py_serial.SERIAL_Init("COM3")

DATA_DIR = "classification_data"
MODEL_DIR = "models"

test_samples = np.load(osp.join(DATA_DIR, "cls_test_samples.npy"))
test_labels = np.load(osp.join(DATA_DIR, "cls_test_labels.npy"))

model = tf.keras.models.load_model(osp.join(MODEL_DIR, "nn_classification_model_keras.h5"))

i = 0
while 1:
    rqType, datalength, dataType = py_serial.SERIAL_PollForRequest()
    if rqType == py_serial.MCU_WRITES:
        # INPUT -> FROM MCU TO PC
        inputs = np.reshape(py_serial.SERIAL_Read(), (1,datalength))
    
    elif rqType == py_serial.MCU_READS:
        # INPUT -> FROM PC TO MCU
        inputs = test_samples[i:i+1].astype(py_serial.SERIAL_GetDType(dataType))
        i = i + 1
        if i >= len(test_samples):
            i = 0
        py_serial.SERIAL_Write(inputs)

    pcout = model.predict(inputs)
    rqType, datalength, dataType = py_serial.SERIAL_PollForRequest()
    if rqType == py_serial.MCU_WRITES:
        mcuout = py_serial.SERIAL_Read()
        print()
        print("Inputs : " + str(inputs))
        print("PC Output : " + str(pcout))
        print("MCU Output : " + str(mcuout))
        print()

        

    