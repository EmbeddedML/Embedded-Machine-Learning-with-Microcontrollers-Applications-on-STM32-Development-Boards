import os

MODEL_DIR = os.path.dirname(__file__)
CLASSIFICATION_MODEL_DIR = os.path.join(MODEL_DIR, "classification_models")
REGRESSION_MODEL_DIR = os.path.join(MODEL_DIR, "regression_models")
CLUSTERING_MODEL_DIR = os.path.join(MODEL_DIR, "clustering_models")
CLASSIFICATION_EXPORT_DIR = os.path.join(MODEL_DIR, "classification_exports")
REGRESSION_EXPORT_DIR = os.path.join(MODEL_DIR, "regression_exports")
CLUSTERING_EXPORT_DIR = os.path.join(MODEL_DIR, "clustering_exports")
TF_MODEL_DIR = os.path.join(MODEL_DIR, "TF_models")
KERAS_MODEL_DIR = os.path.join(TF_MODEL_DIR, "Keras_models")
SAVED_MODEL_DIR = os.path.join(TF_MODEL_DIR, "SavedModels")
TFLITE_MODEL_DIR = os.path.join(MODEL_DIR, "TFLite_models")
TFLITE_EXPORT_DIR = os.path.join(TFLITE_MODEL_DIR, "TFLite_exports")
ONNX_DIR = os.path.join(MODEL_DIR, "ONNX_models")

