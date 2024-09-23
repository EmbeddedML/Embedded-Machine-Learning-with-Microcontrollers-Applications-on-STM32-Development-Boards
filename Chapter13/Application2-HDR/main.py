import os
import tensorflow as tf
import keras
from Models.paths import KERAS_MODEL_DIR

num_classes = 10
(train_images, train_labels), (val_images, val_labels)  = keras.datasets.mnist.load_data()
data_shape = (32, 32, 3)

def prepare_tensor(images, out_shape):
    images = tf.expand_dims(images, axis=-1)
    images = tf.repeat(images, 3, axis=-1)
    images = tf.image.resize(images, out_shape[:2])
    images = images / 255.0
    return images

train_images = prepare_tensor(train_images, data_shape)
val_images = prepare_tensor(val_images, data_shape)

# convert class vectors to binary class matrices
train_labels = keras.utils.to_categorical(train_labels, num_classes)
val_labels = keras.utils.to_categorical(val_labels, num_classes)

mnist_cnn_model = keras.models.load_model(os.path.join(KERAS_MODEL_DIR, "resnet_tl_mnist.h5"))
model_cp_callback = keras.callbacks.ModelCheckpoint(os.path.join(KERAS_MODEL_DIR,"hdr_cnn.h5"), save_best_only=True)
es_callback = keras.callbacks.EarlyStopping(verbose=1, patience=5)
mnist_cnn_model.fit(x = train_images,
                    y = train_labels,
                    epochs=50,
                    validation_data= (val_images, val_labels),
                    verbose=1, 
                    callbacks = [model_cp_callback, es_callback])
