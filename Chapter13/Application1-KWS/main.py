import os
from keras import callbacks
from keras.models import load_model
from Models.paths import KERAS_MODEL_DIR 
from .data_loader import create_datasets

model_path = os.path.join(KERAS_MODEL_DIR, "resnet_tl_mnist.h5")
callback_path = os.path.join(KERAS_MODEL_DIR, "kws_cnn.h5")

train_ds, val_ds, test_ds, input_shape = create_datasets(8000, 512, 256, 32)
kws_cnn_model = load_model(model_path)
model_cp_callback = callbacks.ModelCheckpoint(callback_path, save_best_only=True)
es_callback = callbacks.EarlyStopping(verbose=1, patience=5)
kws_cnn_model.fit(train_ds,
              epochs=50,
              validation_data= val_ds,
              verbose=1, 
              callbacks = [model_cp_callback, es_callback])