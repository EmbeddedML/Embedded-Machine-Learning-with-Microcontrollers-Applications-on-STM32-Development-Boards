import os
from keras.callbacks import ModelCheckpoint, EarlyStopping
from keras.datasets import mnist
from sklearn.model_selection import train_test_split
from Models.paths import KERAS_MODEL_DIR
from .model import RNNMNISTModel

checkpoint_path = os.path.join(KERAS_MODEL_DIR, "hdr_rnn")
(train_imgs, train_labels), (test_imgs, test_labels) = mnist.load_data()
train_imgs = train_imgs / 255.0
test_imgs = test_imgs / 255.0
num_samples, *input_shape = train_imgs.shape
train_imgs, val_imgs, train_labels, val_labels = train_test_split(
    train_imgs, train_labels, test_size=0.1
)

mnist_rnn_model = RNNMNISTModel(input_shape, 10)
model_cp_callback = ModelCheckpoint(checkpoint_path, save_best_only=True)
es_callback = EarlyStopping(verbose=1, patience=5)
mnist_rnn_model.fit(
    x=train_imgs,
    y=train_labels,
    epochs=50,
    validation_data=(val_imgs, val_labels),
    verbose=1,
    callbacks=[model_cp_callback, es_callback],
)
