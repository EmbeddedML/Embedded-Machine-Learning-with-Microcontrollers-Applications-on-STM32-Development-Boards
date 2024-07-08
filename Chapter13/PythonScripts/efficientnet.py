# /*---------------------------------------------------------------------------------------------
#  * Copyright 2015 The TensorFlow Authors. 
#  * Copyright (c) 2022 STMicroelectronics.
#  * All rights reserved.
#  *
#  * This software is licensed under terms that can be found in the LICENSE file in
#  * the root directory of this software component.
#  * If no LICENSE file comes with this software, it is provided AS-IS.
#  *--------------------------------------------------------------------------------------------*/

import tensorflow as tf
from keras import layers
from typing import List, Tuple
import math
from keras.models import Model

repeats = [1, 2, 2, 3, 3, 4, 1]


def round_expansion(expansion_factor: int, repeats: List[int]) -> List[int] :
    exp_ratio = []
    flag = 1
    for r in repeats:
        if (r != 0) and flag:
            exp_ratio.append(1)
            flag = 0
        else:
            exp_ratio.append(expansion_factor)

    return exp_ratio


def round_filters(filters: int, width_coefficient: float, depth_divisor: int = 8, min_filters: int = None) -> int:
    """Round number of filters based on depth multiplier."""
    if not width_coefficient:
        return filters
    filters *= width_coefficient
    min_filters = min_filters or depth_divisor
    new_filters = max(int(filters + depth_divisor / 2) // depth_divisor * depth_divisor, min_filters)
    # Make sure that round down does not go down by more than 10%.
    if new_filters < 0.9 * filters:
        new_filters += depth_divisor
    return int(new_filters)


def round_repeats(repeats: List[int]) -> List[int]:
    num_repeat = sum(repeats)
    num_repeat_scaled = int(math.ceil(num_repeat))
    repeats_scaled = []
    for r in repeats[::-1]:
        rs = max(1, round((r / num_repeat * num_repeat_scaled)))
        repeats_scaled.append(rs)
        num_repeat -= r
        num_repeat_scaled -= rs
    repeats_scaled = repeats_scaled[::-1]
    return repeats_scaled    

def mb_conv_block(inputs: tf.Tensor, in_channels: int, out_channels: int, num_repeat: int, stride: int, expansion_factor: int, se_ratio: float, k: int, drop_rate: float, 
                  prev_block_num: int, activation) -> tf.Tensor:

    x = inputs
    input_filters = in_channels
	
    for i in range(num_repeat):
        input_tensor = x
        if i == 0:
            stride = stride
        else:
            stride = 1

        expanded_filters = input_filters * expansion_factor
        if expansion_factor != 1:
            x = layers.Conv2D(filters=expanded_filters, kernel_size=(1, 1), strides=1, padding='same')(x)
            x = layers.BatchNormalization()(x)
            x = layers.Activation(activation)(x)

        x = layers.DepthwiseConv2D(kernel_size=(k, k), strides=stride, padding='same')(x)
        x = layers.BatchNormalization()(x)
        x = layers.Activation(activation)(x)

        squeezed_filters = max (1, int(input_filters * se_ratio))
        se_tensor = layers.GlobalAveragePooling2D()(x)
        se_tensor = layers.Reshape((1, 1, expanded_filters))(se_tensor)
        se_tensor = layers.Conv2D(filters=squeezed_filters , kernel_size=(1, 1), padding='same')(se_tensor)
        se_tensor = layers.Activation(activation, name='act_{}'.format(i+prev_block_num))(se_tensor)
        se_tensor = layers.Conv2D(filters=expanded_filters , kernel_size=(1, 1), padding='same')(se_tensor)
		
        # se_tensor = layers.Lambda(lambda x: tf.clip_by_value(x, clip_value_min=-4.0, clip_value_max=4.0))(se_tensor)
        se_tensor = layers.Minimum()([se_tensor, tf.fill(se_tensor.shape[1:], 4.0)])
        se_tensor = layers.Maximum()([se_tensor, tf.fill(se_tensor.shape[1:], -4.0)])
        se_tensor = layers.Activation('sigmoid', name='act2_{}'.format(i+prev_block_num))(se_tensor)
        x = layers.multiply([x, se_tensor])
        
        x = layers.Conv2D(filters=out_channels, kernel_size=(1, 1), strides=1, padding='same')(x)
        x = layers.BatchNormalization()(x)

        if stride == 1 and input_filters == out_channels:
            num_blocks_total = 16
            dropout_rate = drop_rate * float(prev_block_num + i) / num_blocks_total
            if dropout_rate and (dropout_rate > 0):
                x = layers.Dropout(dropout_rate, noise_shape=(None, 1, 1, 1))(x)
            x = layers.add([x, input_tensor])
            
        input_filters = out_channels

    return x


def EfficientNet(input_shape: Tuple[int, int, int] = (32,32,3),
                 classes: int = 10,
                 dropout_rate: float = 0.2,
                 se_ratio: float = 0.25,
                 drop_connect_rate: float = 0.2,
                 ) -> Model:

    # Determine proper input shape
    input = layers.Input(shape=input_shape)

    # Build stem
    x = layers.Conv2D(filters=round_filters(32, .45), kernel_size=(3, 3), strides=(2, 2), padding='same')(input)
    x = layers.BatchNormalization()(x)
    x = layers.Activation(tf.nn.relu6, name='stem_activation')(x)

    # Build blocks
    repeats_scaled = round_repeats(repeats)
    exp_ratio = round_expansion(3, repeats_scaled)
    
    block1 = mb_conv_block(inputs=x, in_channels=round_filters(32, .45), out_channels=round_filters(16, .45), 
                           num_repeat=repeats_scaled[0],stride=1, expansion_factor=exp_ratio[0], se_ratio=se_ratio, k=3, drop_rate=drop_connect_rate, 
                           prev_block_num=0, activation=tf.nn.relu6)

    block2 = mb_conv_block(inputs=block1, in_channels=round_filters(16, .45), out_channels=round_filters(24, .45), 
                           num_repeat=repeats_scaled[1],stride=2, expansion_factor=exp_ratio[1], se_ratio=se_ratio, k=3, drop_rate=drop_connect_rate, 
                           prev_block_num=sum(repeats_scaled[0:1]), activation=tf.nn.relu6)
    
    block3 = mb_conv_block(inputs=block2, in_channels=round_filters(24, .45), out_channels=round_filters(40, .45), 
                           num_repeat=repeats_scaled[2],stride=2, expansion_factor=exp_ratio[2], se_ratio=se_ratio, k=5, drop_rate=drop_connect_rate, 
                           prev_block_num=sum(repeats_scaled[0:2]), activation=tf.nn.relu6)
    
    block4 = mb_conv_block(inputs=block3, in_channels=round_filters(40, .45), out_channels=round_filters(80, .45), 
                           num_repeat=repeats_scaled[3], stride=2, expansion_factor=exp_ratio[3], se_ratio=se_ratio, k=3, drop_rate=drop_connect_rate, 
                           prev_block_num=sum(repeats_scaled[0:3]), activation=tf.nn.relu6)
    
    block5 = mb_conv_block(inputs=block4, in_channels=round_filters(80, .45), out_channels=round_filters(112, .45), 
                           num_repeat=repeats_scaled[4], stride=1, expansion_factor=exp_ratio[4], se_ratio=se_ratio, k=5, drop_rate=drop_connect_rate, 
                           prev_block_num=sum(repeats_scaled[0:4]), activation=tf.nn.relu6)
    
    block6 = mb_conv_block(inputs=block5, in_channels=round_filters(112, .45), out_channels=round_filters(192, .45),
                            num_repeat=repeats_scaled[5], stride=2, expansion_factor=exp_ratio[5], se_ratio=se_ratio, k=5, drop_rate=drop_connect_rate, 
                            prev_block_num=sum(repeats_scaled[0:5]), activation=tf.nn.relu6)
    
    block7 = mb_conv_block(inputs=block6, in_channels=round_filters(192, .45), out_channels=round_filters(320, .45),
                            num_repeat=repeats_scaled[6],stride=1, expansion_factor=exp_ratio[6], se_ratio=se_ratio, k=3, drop_rate=drop_connect_rate, 
                            prev_block_num=sum(repeats_scaled[0:6]), activation=tf.nn.relu6)

    # Build top
    x = layers.Conv2D(filters=round_filters(1280, .45), kernel_size=(1, 1), padding='same', name='top_conv')(block7)
    x = layers.BatchNormalization()(x)
    x = layers.Activation(tf.nn.relu6, name='top_activation')(x)
	
    x = layers.GlobalAveragePooling2D(name='avg_pool')(x)
    if dropout_rate and dropout_rate > 0:
        x = layers.Dropout(dropout_rate, name='top_dropout')(x)
    x = layers.Dense(classes, activation='softmax', name='output_probs')(x)

    model = Model(input, x, name="EfficientNet-STCustom")

    return model