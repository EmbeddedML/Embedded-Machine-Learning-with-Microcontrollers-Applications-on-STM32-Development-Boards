import os
import sys
import numpy as np
from sklearn2c import SVMClassifier
sys.path.append("Common")
import py_serial 

dirname = os.path.dirname
py_serial.SERIAL_Init("COM3")

test_samples = np.load(os.path.join(dirname(__file__),"classification_data","cls_test_samples.npy"))
test_labels = np.load(os.path.join(dirname(__file__),"classification_data","cls_test_labels.npy"))

svm = SVMClassifier.load(os.path.join(dirname(__file__),"classification_models", "svm_classifier.joblib"))

i = 0
while 1:
    rqType, datalength, dataType = py_serial.SERIAL_PollForRequest()
    if rqType == py_serial.MCU_WRITES:
        # INPUT -> FROM MCU TO PC
        inputs = py_serial.SERIAL_Read()
    
    elif rqType == py_serial.MCU_READS:
        # INPUT -> FROM PC TO MCU
        inputs = test_samples[i:i+1].astype(py_serial.SERIAL_GetDType(dataType))
        i = i + 1
        if i >= len(test_samples):
            i = 0
        py_serial.SERIAL_Write(inputs)

    pcout = svm.score(np.reshape(inputs, (1, datalength)))
    rqType, datalength, dataType = py_serial.SERIAL_PollForRequest()
    if rqType == py_serial.MCU_WRITES:
        mcuout = py_serial.SERIAL_Read()
        print()
        print("Inputs : " + str(inputs))
        print("PC Output : " + str(pcout))
        print("MCU Output : " + str(mcuout))
        print()

        

    