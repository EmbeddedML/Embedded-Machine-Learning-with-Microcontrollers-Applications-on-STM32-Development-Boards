import tensorflow as tf

# Convert a saved model
saved_model_dir='models/nn_classification_model_tf'

# Dynamic range quantization
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model_quant = converter.convert()

# Save the model.
with open('models/quantized_model_dyn_range.tflite', 'wb') as f:
  f.write(tflite_model_quant)