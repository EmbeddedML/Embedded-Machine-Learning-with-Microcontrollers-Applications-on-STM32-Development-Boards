import os
import onnx2tf
from Models.paths import ONNX_DIR, KERAS_MODEL_DIR

onnx2tf.convert(
    input_onnx_file_path= os.path.join(ONNX_DIR, "mobilenetv3small.onnx"),
    output_folder_path=os.path.join(KERAS_MODEL_DIR, "mobilenetv3small"),
    output_h5=True,
    non_verbose=True,
)
