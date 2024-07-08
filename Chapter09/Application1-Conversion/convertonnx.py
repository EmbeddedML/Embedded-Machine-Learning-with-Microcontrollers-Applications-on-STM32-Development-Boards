import onnx2tf

onnx2tf.convert(
    input_onnx_file_path="mobilenetv3small.onnx",
    output_folder_path="mobilenetv3small_tf",
    output_h5=True,
    non_verbose=True,
)
