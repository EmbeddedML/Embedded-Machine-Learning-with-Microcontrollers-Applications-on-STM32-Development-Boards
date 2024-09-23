from keras.models import Sequential
from keras.layers import Dense, GRU, Dropout
from keras.optimizers import Adam
from keras.losses import MeanAbsoluteError

def gru_temperature_model(input_shape):
    model = Sequential([GRU(units = 50, return_sequences = True, input_shape = (input_shape,1), unroll = True),
                        Dropout(0.2),
                        GRU(units = 50, unroll= True),
                        Dense(units = 1)])

    model.compile(optimizer=Adam(learning_rate=5e-4),
                  loss=MeanAbsoluteError())
    return model
