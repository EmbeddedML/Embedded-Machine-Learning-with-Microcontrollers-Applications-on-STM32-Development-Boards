from data_loader import create_datasets
from model import RNNKWSModel
from keras import callbacks

SAMPLE_RATE = 8000
FFT_LEN = 512
STEP_SIZE = 256
BATCH_SIZE = 32
NUM_MEL_BINS = 80

train_ds, val_ds, test_ds, input_shape = create_datasets(SAMPLE_RATE, FFT_LEN, STEP_SIZE, BATCH_SIZE, NUM_MEL_BINS)

kws_rnn_model = RNNKWSModel(10, input_shape)

model_cp_callback = callbacks.ModelCheckpoint("kws_rnn_model.h5", save_best_only=True)
es_callback = callbacks.EarlyStopping(verbose=1, patience=5)

kws_rnn_model.summary()

kws_rnn_model.fit(train_ds,
              epochs=50,
              validation_data= val_ds,
              verbose=1, 
              callbacks = [model_cp_callback, es_callback])
