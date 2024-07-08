import keras
from sklearn.model_selection import train_test_split
from model import RNNMNISTModel

(train_imgs, train_labels), (test_imgs, test_labels) = keras.datasets.mnist.load_data()
train_imgs = train_imgs / 255.0
test_imgs = test_imgs / 255.0
num_samples, *input_shape = train_imgs.shape
train_imgs, val_imgs, train_labels, val_labels = train_test_split(
    train_imgs, train_labels, test_size=0.1
)

mnist_rnn_model = RNNMNISTModel(input_shape, 10)
model_cp_callback = keras.callbacks.ModelCheckpoint(
    "mnist_rnn_model.h5", save_best_only=True
)
es_callback = keras.callbacks.EarlyStopping(verbose=1, patience=5)
mnist_rnn_model.fit(
    x=train_imgs,
    y=train_labels,
    epochs=50,
    validation_data=(val_imgs, val_labels),
    verbose=1,
    callbacks=[model_cp_callback, es_callback],
)
