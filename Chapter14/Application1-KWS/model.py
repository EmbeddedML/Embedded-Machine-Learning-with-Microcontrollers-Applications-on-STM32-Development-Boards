from keras import layers
from keras import Model

def RNNKWSModel(nCategories, input_shape):
    inputs = layers.Input(input_shape, name='input')
    x = layers.Conv2D(10, (5, 1), activation='relu', padding='same')(inputs)
    x = layers.BatchNormalization()(x)
    x = layers.Conv2D(1, (5, 1), activation='relu', padding='same')(x)
    x = layers.BatchNormalization()(x)
    x = layers.Reshape(input_shape[0:2])(x)
    x = layers.LSTM(128, return_sequences=True, unroll = True)(x)
    x = layers.LSTM(128, return_sequences=True, unroll = True)(x)
    xFirst = x[:, -1]
    query = layers.Dense(128)(xFirst)

    scores = layers.Dot(axes=[1, 2])([query, x])
    scores = layers.Softmax(name='softmax')(scores)  
    attVector = layers.Dot(axes=[1, 1])([scores, x])

    x = layers.Dense(64, activation='relu')(attVector)
    x = layers.Dense(32)(x)

    output = layers.Dense(nCategories, activation='softmax', name='output')(x)

    model = Model(inputs=[inputs], outputs=[output])
    model.compile(optimizer='adam', loss=['sparse_categorical_crossentropy'], metrics=['sparse_categorical_accuracy'])

    return model