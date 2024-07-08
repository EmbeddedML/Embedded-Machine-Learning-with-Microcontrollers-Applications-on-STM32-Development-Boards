from keras.applications import MobileNetV2
from keras import layers
from keras import Model

def make_divisible(v, divisor, min_value=None):
    if min_value is None:
        min_value = divisor

    new_v = max(min_value, int(v + divisor / 2) // divisor * divisor)

    if new_v < 0.9 * v:
        new_v += divisor
    return new_v


def mobileNetV2(input_shape, num_classes, alpha=0.35, dropout=None):
    
    feature_extractor = MobileNetV2(
        input_shape= input_shape,
        alpha=alpha,
        include_top=False,
    )
    
    x = feature_extractor.output
    last_block_filters = make_divisible(1280 * alpha, 8)
    x = layers.Conv2D(last_block_filters, kernel_size=1, padding='same', use_bias=False)(x)
    x = layers.BatchNormalization()(x)
    x = layers.ReLU(6.)(x)

    x = layers.GlobalAveragePooling2D()(x)
    if dropout:
        x = layers.Dropout(rate=dropout, name="dropout")(x)
    outputs = layers.Dense(num_classes, activation="softmax")(x)

    return Model(inputs = feature_extractor.input, outputs=outputs)