import os.path as osp
import numpy as np
import tensorflow as tf

DATA_DIR = "classification_data"
MODEL_DIR = "models"

saved_model_dir='models/nn_classification_model_tf'

train_samples = np.load(osp.join(DATA_DIR, "cls_train_samples.npy"))
train_labels = np.load(osp.join(DATA_DIR, "cls_train_labels.npy"))
test_samples = np.load(osp.join(DATA_DIR, "cls_test_samples.npy"))
test_labels = np.load(osp.join(DATA_DIR, "cls_test_labels.npy"))

# test the actual model on a test sample image
model = tf.keras.models.load_model(saved_model_dir)

predictions = model.predict(test_samples)
predicted_labels = np.where(predictions < 0.5, 0, 1).squeeze()

tflite_model_file= osp.join("models","nn_classification_model.tflite")

# Convert test_samples to float32 format
test_samples = test_samples.astype(np.float32)
accuracy = (np.sum(test_labels == predicted_labels) * 100) / len(test_samples)

# Helper function to run inference on a TFLite model
def tflite_predict(lite_model_path):
    # Initialize the interpreter
    interpreter = tf.lite.Interpreter(model_path=str(lite_model_path))
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()[0]
    output_details = interpreter.get_output_details()[0]
        
    # Check if the input type is quantized, then rescale input data to uint8
    tflite_preds = np.empty_like(test_labels, dtype=int)
    for idx, test_sample in enumerate(test_samples):
        if input_details['dtype'] == np.uint8:
            input_scale, input_zero_point = input_details["quantization"]
            test_sample = test_sample / input_scale + input_zero_point

        interpreter.set_tensor(input_details["index"], [test_sample])
        interpreter.invoke()
        output = interpreter.get_tensor(output_details["index"])[0]
        tflite_preds[idx] = 0 if output < .5 else 1

    return tflite_preds

def evaluate_model(tflite_file):
  tflite_preds = tflite_predict(tflite_file)

  accuracy = (np.sum(test_labels== tflite_preds) * 100) / len(test_samples)
  return accuracy
  
tflite_accuracy = evaluate_model(tflite_model_file)

print(f"Keras model accuracy is {accuracy:.2f}% (Number of test samples={len(test_samples)})")
print(f"TFlite model accuracy is {tflite_accuracy:.2f}% (Number of test samples={len(test_samples)})")