import os
import keras
from Models.paths import KERAS_MODEL_DIR, SAVED_MODEL_DIR

input = keras.Input(shape=(32,))
output = keras.layers.Dense(1)(input)
model = keras.Model(input, output)
model.compile(optimizer="adam", loss="mean_squared_error")

# Saves model in Keras h5 format
model.save(os.path.join(KERAS_MODEL_DIR, "tf_save_model.h5"))

# Saves model in TF SavedModel format
model.save(os.path.join(SAVED_MODEL_DIR, "tf_save_model"))