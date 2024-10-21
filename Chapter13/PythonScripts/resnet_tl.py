import os
import tensorflow as tf
from keras.utils import get_file
from Models.paths import KERAS_MODEL_DIR
from .resnet import ResNet

model_checkpoint_path = os.path.join(KERAS_MODEL_DIR, "resnet_tl_mnist.h5")

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

model = ResNet(num_classes, data_shape, 8, 0.15)
pretrained_model_path = get_file(origin = "https://github.com/STMicroelectronics/stm32ai-modelzoo/raw/main/image_classification/pretrained_models/resnetv1/ST_pretrainedmodel_public_dataset/cifar10/resnet_v1_8_32_tfs/resnet_v1_8_32_tfs.h5",
                                 cache_subdir= "models")

model.load_weights(pretrained_model_path)
num_layers_to_train = len(model.layers)//3
for layer in model.layers[:num_layers_to_train]:
    layer.trainable = False

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
    validation_data=(test_images, test_labels),
    callbacks=callbacks,
)