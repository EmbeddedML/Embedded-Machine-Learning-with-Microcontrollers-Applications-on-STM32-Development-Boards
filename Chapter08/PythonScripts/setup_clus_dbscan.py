import os
from sklearn2c.clustering import Dbscan
import py_serial
import numpy as np
from Data.paths import CLASSIFICATION_DATA_DIR
from Models.paths import CLUSTERING_MODEL_DIR

py_serial.SERIAL_Init("COM4")

test_samples = np.load(os.path.join(CLASSIFICATION_DATA_DIR,"cls_test_samples.npy"))
test_labels = np.load(os.path.join(CLASSIFICATION_DATA_DIR,"cls_test_labels.npy"))

dbscan_model_dir = os.path.join(CLUSTERING_MODEL_DIR, "dbscan_clustering.joblib")
dbscan = Dbscan.load(dbscan_model_dir)

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
    
    pcout = dbscan.predict(np.reshape(inputs, (1, datalength)).astype(np.double))
    rqType, datalength, dataType = py_serial.SERIAL_PollForRequest()
    if rqType == py_serial.MCU_WRITES:
        mcuout = py_serial.SERIAL_Read()
        print()
        print("Inputs : " + str(inputs))
        print("PC Output : " + str(pcout))
        print("MCU Output : " + str(mcuout))
        print()

        