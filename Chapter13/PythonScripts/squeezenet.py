import tensorflow as tf
from keras.utils import get_file

WEIGHTS_PATH_NO_TOP = "https://github.com/rcmalli/keras-squeezenet/releases/download/v1.0/squeezenet_weights_tf_dim_ordering_tf_kernels_notop.h5"


def fire(x, squeeze, expand, name):
    y = tf.keras.layers.Conv2D(
        filters=squeeze,
        kernel_size=1,
        activation="relu",
        padding="same",
        name=f"{name}_squeeze")(x)
    y1 = tf.keras.layers.Conv2D(
        filters=expand,
        kernel_size=1,
        activation="relu",
        padding="same",
        name=f"{name}_expand1x1",
    )(y)
    y3 = tf.keras.layers.Conv2D(
        filters=expand,
        kernel_size=3,
        activation="relu",
        padding="same",
        name=f"{name}_expand3x3",
    )(y)
    return tf.keras.layers.concatenate([y1, y3], name=f"{name}_concat")

def SqueezeNet(input_shape=(224, 224, 3), weights="imagenet", classes=10, dropout = None):
    model_input = tf.keras.layers.Input(shape=input_shape)
    x = tf.keras.layers.Conv2D(64, (3, 3), strides=2, padding="valid", activation="relu", name = "conv1")(model_input)
    x = tf.keras.layers.MaxPooling2D((3, 3), strides=2, padding="same")(x)
    x = fire(x, 16, 64, name="fire1")
    x = fire(x, 16, 64, name="fire2")
    x = tf.keras.layers.MaxPooling2D((3, 3), strides=2, padding="same")(x)
    x = fire(x, 32, 128, name="fire3")
    x = fire(x, 32, 128, name="fire4")
    x = tf.keras.layers.MaxPooling2D((3, 3), strides=2, padding="same")(x)
    x = fire(x, 48, 192, name="fire5")
    x = fire(x, 48, 192, name="fire6")
    x = fire(x, 64, 256, name="fire7")
    feature_extractor = fire(x, 64, 256, name="fire8")

    feature_ext_model = tf.keras.Model(inputs=[model_input], outputs=[feature_extractor])
    if dropout:
        x = tf.keras.layers.Dropout(dropout, name='drop9')(x)

    if weights == "imagenet":
        weights_path = get_file(
            "squeezenet_weights_tf_dim_ordering_tf_kernels_notop.h5",
            WEIGHTS_PATH_NO_TOP,
            cache_subdir="models",
        )

        feature_ext_model.load_weights(weights_path)
                
    feature_extractor_out = feature_ext_model.output 
    x = tf.keras.layers.Conv2D(classes, (1, 1), name = "final_conv")(feature_extractor_out)
    x = tf.keras.layers.GlobalAveragePooling2D(name="global_avg_pool")(x)
    model_output = tf.keras.layers.Softmax()(x)
    model = tf.keras.Model(inputs = [model_input], outputs = [model_output])

    return model