import keras

input = keras.Input(shape=(32,))
output = keras.layers.Dense(1)(input)
model = keras.Model(input, output)
model.compile(optimizer="adam", loss="mean_squared_error")

# Saves model in Keras h5 format
model.save("model.h5")

# Saves model in TF SavedModel format
model.save("model")