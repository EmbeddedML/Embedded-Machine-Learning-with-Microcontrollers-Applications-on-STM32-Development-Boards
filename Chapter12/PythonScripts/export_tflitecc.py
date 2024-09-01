import tensorflow as tf
from tflite2cc import convert_tflite2cc

# Convert a saved model
saved_model_dir='models/nn_classification_model_tf'
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir) 
tflite_model = converter.convert()

tflite_model_file= 'models/nn_classification_model.tflite' 

# Save the TF Lite model
with open(tflite_model_file, 'wb') as f:
  f.write(tflite_model)

C_filepath = "models/classification"

convert_tflite2cc(tflite_model, c_out= C_filepath)