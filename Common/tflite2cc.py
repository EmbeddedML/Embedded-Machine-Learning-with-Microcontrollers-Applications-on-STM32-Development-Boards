import os
from typing import Union


def convert_tflite2cc(tflite_model: Union[str, bytes], c_out: str):
    if type(tflite_model) == str:
        with open(tflite_model, "rb") as tflite_file:
            tflite_model = tflite_file.read()

    hdr_filepath = c_out + ".h"
    src_filepath = c_out + ".cpp"
    hdr_filename = os.path.basename(hdr_filepath)

    arr_len = len(tflite_model)
    with open(hdr_filepath, "w") as hdr_file:
        hdr_file.write("extern const unsigned char converted_model_tflite[];\n")
        hdr_file.write("extern const unsigned int converted_model_tflite_len;\n")

    with open(src_filepath, "w") as src_file:
        src_file.write(f'#include "{hdr_filename}"\n')
        src_file.write("const unsigned char converted_model_tflite[] = {")
        for i in range(0, arr_len, 15):
            src_file.write(",".join(hex(x) for x in tflite_model[i : i + 15]) + ",\n")
        src_file.write(
            f"}};\nconst unsigned int converted_model_tflite_len = {arr_len};"
        )
