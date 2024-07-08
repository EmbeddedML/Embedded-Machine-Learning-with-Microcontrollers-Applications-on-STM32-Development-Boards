import tensorflow as tf

# Convert a saved model
saved_model_dir='models/nn_classification_model_tf'
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir) 
tflite_model = converter.convert()

# Save the TF Lite model
with open('models/nn_classification_model.tflite', 'wb') as f:
  f.write(tflite_model)