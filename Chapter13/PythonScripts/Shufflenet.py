import tensorflow as tf
from keras.models import Model
import numpy as np


def ShuffleNet(
    include_top=True,
    scale_factor=1.0,
    pooling="max",
    input_shape=(224, 224, 3),
    groups=1,
    model_weights=None,
    num_shuffle_units=[3, 7, 3],
    bottleneck_ratio=0.25,
    classes=1000,
):
    shuffle_unit_str = "".join([str(x) for x in num_shuffle_units])
    name = (
        f"ShuffleNet_{scale_factor:.2g}X_g{groups}_br_{bottleneck_ratio}_{shuffle_unit_str}"
    )

    out_dim_stage_two = {1: 144, 2: 200, 3: 240, 4: 272, 8: 384}

    if pooling not in ["max", "avg"]:
        raise ValueError("Invalid value for pooling.")

    if not (float(scale_factor) * 4).is_integer():
        raise ValueError("Invalid value for scale_factor. Should be x over 4.")

    exp = np.insert(np.arange(0, len(num_shuffle_units), dtype=np.float32), 0, 0)
    out_channels_in_stage = 2**exp
    out_channels_in_stage *= out_dim_stage_two[
        groups
    ]  # calculate output channels for each stage
    out_channels_in_stage[0] = 24  # first stage has always 24 output channels
    out_channels_in_stage *= scale_factor
    out_channels_in_stage = out_channels_in_stage.astype(int)

    img_input = tf.keras.layers.Input(shape=input_shape)

    # create shufflenet architecture
    x = tf.keras.layers.Conv2D(
        filters=out_channels_in_stage[0],
        kernel_size=(3, 3),
        padding="same",
        use_bias=False,
        strides=(2, 2),
        activation="relu",
        name="conv1",
    )(img_input)
    x = tf.keras.layers.MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding="same", name="maxpool1")(
        x
    )

    # create stages containing shufflenet units beginning at stage 2
    for stage in range(0, len(num_shuffle_units)):
        repeat = num_shuffle_units[stage]
        x = _block(
            x,
            out_channels_in_stage,
            repeat=repeat,
            bottleneck_ratio=bottleneck_ratio,
            groups=groups,
            stage=stage + 2,
        )

    if pooling == "avg":
        x = tf.keras.layers.GlobalAveragePooling2D(name="global_pool")(x)
    elif pooling == "max":
        x = tf.keras.layers.GlobalMaxPooling2D(name="global_pool")(x)

    if include_top:
        x = tf.keras.layers.Dense(units=classes, name="fc", activation="softmax")(x)

    inputs = img_input
    model = Model(inputs=inputs, outputs=x, name=name)

    if model_weights is not None:
        model.load_weights(model_weights)

    return model


def _block(x, channel_map, bottleneck_ratio, repeat=1, groups=1, stage=1):
    x = _shuffle_unit(
        x,
        in_channels=channel_map[stage - 2],
        out_channels=channel_map[stage - 1],
        strides=2,
        groups=groups,
        bottleneck_ratio=bottleneck_ratio,
        stage=stage,
        block=1,
    )

    for i in range(1, repeat + 1):
        x = _shuffle_unit(
            x,
            in_channels=channel_map[stage - 1],
            out_channels=channel_map[stage - 1],
            strides=1,
            groups=groups,
            bottleneck_ratio=bottleneck_ratio,
            stage=stage,
            block=(i + 1),
        )

    return x


def _shuffle_unit(
    inputs,
    in_channels,
    out_channels,
    groups,
    bottleneck_ratio,
    strides=2,
    stage=1,
    block=1,
):
    prefix = f"stage{stage}/block{block}"

    bottleneck_channels = int(out_channels * bottleneck_ratio)
    groups = 1 if stage == 2 and block == 1 else groups

    x = _group_conv(
        inputs,
        in_channels,
        out_channels=bottleneck_channels,
        groups=(1 if stage == 2 and block == 1 else groups),
        name=f"{prefix}/1x1_gconv_1",
    )
    x = tf.keras.layers.BatchNormalization(name=f"{prefix}/bn_gconv_1")(x)
    x = tf.keras.layers.Activation("relu", name=f"{prefix}/relu_gconv_1")(x)

    height, width, group_channels = x.shape.as_list()[1:]
    channels_per_group = group_channels // groups

    x = tf.reshape(x, [-1, height, width, groups, channels_per_group])
    x = tf.transpose(x, (0, 1, 2, 4, 3))
    x = tf.reshape(x, [-1, height, width, group_channels])
    x = tf.keras.layers.DepthwiseConv2D(
        kernel_size=(3, 3),
        padding="same",
        use_bias=False,
        strides=strides,
        name=f"{prefix}/1x1_dwconv_1",
    )(x)
    x = tf.keras.layers.BatchNormalization(name=f"{prefix}/bn_dwconv_1")(x)

    x = _group_conv(
        x,
        bottleneck_channels,
        out_channels=out_channels if strides == 1 else out_channels - in_channels,
        groups=groups,
        name=f"{prefix}/1x1_gconv_2",
    )
    x = tf.keras.layers.BatchNormalization(name=f"{prefix}/bn_gconv_2")(x)

    if strides < 2:
        ret = tf.keras.layers.Add(name=f"{prefix}/add")([x, inputs])
    else:
        avg = tf.keras.layers.AveragePooling2D(
            pool_size=3, strides=2, padding="same", name=f"{prefix}/avg_pool"
        )(inputs)
        ret = tf.keras.layers.Concatenate(name=f"{prefix}/concat")([x, avg])

    ret = tf.keras.layers.Activation("relu", name=f"{prefix}/relu_out")(ret)

    return ret


def _group_conv(x, in_channels, out_channels, groups, kernel=1, stride=1, name=""):
    if groups == 1:
        return tf.keras.layers.Conv2D(
            filters=out_channels,
            kernel_size=kernel,
            padding="same",
            use_bias=False,
            strides=stride,
            name=name,
        )(x)

    # number of intput channels per group
    ig = in_channels // groups
    group_list = []

    assert out_channels % groups == 0

    for i in range(groups):
        offset = i * ig
        group = tf.gather(x, np.arange(offset, offset + ig), axis = 3)
        group_list.append(
            tf.keras.layers.Conv2D(
                int(0.5 + out_channels / groups),
                kernel_size=kernel,
                strides=stride,
                use_bias=False,
                padding="same",
                name=f"{name}_/g{i}"
            )(group)
        )
    return tf.keras.layers.Concatenate(name=f"{name}/concat")(group_list)