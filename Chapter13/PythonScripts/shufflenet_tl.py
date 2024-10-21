import os
import tensorflow as tf
from Models.paths import KERAS_MODEL_DIR
from .shufflenet import ShuffleNet

model_checkpoint_path = os.path.join(KERAS_MODEL_DIR, "shufflenet_tl_mnist.h5")

num_classes = 10
(train_images, train_labels), (
    test_images,
    test_labels,
) = tf.keras.datasets.mnist.load_data()

data_shape = (32, 32, 3)

def prepare_tensor(images, out_shape):
    images = tf.expand_dims(images, axis=-1)
    images = tf.repeat(images, 3, axis=-1)
    images = tf.image.resize(images, out_shape[:2])
    images = images / 255.0
    return images


train_images = prepare_tensor(train_images, data_shape)
test_images = prepare_tensor(test_images, data_shape)

# convert class vectors to binary class matrices
train_labels = tf.keras.utils.to_categorical(train_labels, num_classes)
test_labels = tf.keras.utils.to_categorical(test_labels, num_classes)
model = ShuffleNet(
    scale_factor = 0.25,
    groups = 3,
    input_shape=data_shape,
    classes = 10
)

# feature_extractor.trainable = False
# x = tf.keras.layers.Dense(100, activation="relu")(feature_extractor.output)
# model_output = tf.keras.layers.Dense(10, activation="softmax")(x)

# model = tf.keras.Model(inputs = [feature_extractor.input], outputs = [model_output])

model.summary()
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
callbacks = [
    tf.keras.callbacks.ModelCheckpoint(
        model_checkpoint_path,
        monitor="val_loss",
        save_best_only=True,
        mode="min",
        verbose=1,
    )
]
history = model.fit(
    train_images,
    train_labels,
    batch_size=128,
    epochs=10,
    validation_split=0.1,
    callbacks=callbacks,
)
