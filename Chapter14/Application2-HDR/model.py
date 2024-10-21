from keras import Input
from keras import layers
from keras import Model
from keras.optimizers import Adam

def RNNMNISTModel(input_shape, num_classes):
    inp = Input(input_shape)
    state = layers.LSTM(16, unroll=True)(inp)
    output = layers.Dense(num_classes, activation="softmax")(state)
    model = Model(inputs=[inp], outputs=[output])
    opt = Adam(learning_rate=1e-3)
    model.compile(
        optimizer=opt,
        loss=["sparse_categorical_crossentropy"],
        metrics=["sparse_categorical_accuracy"],
    )
    return model
