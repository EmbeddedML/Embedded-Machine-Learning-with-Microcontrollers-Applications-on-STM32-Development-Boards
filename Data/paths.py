import os
parent = os.path.dirname

DATA_DIR = parent(__file__)
CLASSIFICATION_DATA_DIR =  os.path.join(DATA_DIR, "classification_data")
REGRESSION_DATA_DIR = os.path.join(DATA_DIR, "regression_data")
WISDM_PATH = os.path.join(DATA_DIR, "WISDM_ar_v1.1", "WISDM_ar_v1.1_raw.txt")
FSDD_PATH = os.path.join(DATA_DIR, "FSDD")
MNIST_PATH = os.path.join(DATA_DIR, "MNIST")
TEMPERATURE_DATA_PATH = os.path.join(DATA_DIR, "temperature_dataset.csv")
RGB_IMAGE_PATH = os.path.join(DATA_DIR, "im_rgb.jpg")