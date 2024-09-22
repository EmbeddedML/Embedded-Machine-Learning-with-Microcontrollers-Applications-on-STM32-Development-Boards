from keras import callbacks
from keras.models import load_model
from .data_loader import create_datasets

train_ds, val_ds, test_ds, input_shape = create_datasets(8000, 512, 256, 32)
kws_cnn_model = load_model("resnet_tl_mnist.h5")
model_cp_callback = callbacks.ModelCheckpoint("kws_cnn_model.h5",save_best_only=True)
es_callback = callbacks.EarlyStopping(verbose=1, patience=5)
kws_cnn_model.fit(train_ds,
              epochs=50,
              validation_data= val_ds,
              verbose=1, 
              callbacks = [model_cp_callback, es_callback])