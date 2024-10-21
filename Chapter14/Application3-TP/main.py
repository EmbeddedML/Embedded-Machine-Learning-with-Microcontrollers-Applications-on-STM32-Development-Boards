
import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from .model import gru_temperature_model
from Data.paths import TEMPERATURE_DATA_PATH
from Models.paths import KERAS_MODEL_DIR

df = pd.read_csv(TEMPERATURE_DATA_PATH)
y = df['Room_Temp']
prev_values_count = 5

X = pd.DataFrame()
for i in range(prev_values_count, 0, -1):
    X['t-' + str(i)] = y.shift(i)

X = X[prev_values_count:]
y = y[prev_values_count:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
train_mean = X_train.mean()
train_std = X_train.std()

X_train = (X_train - train_mean)/ train_std
X_test = (X_test - train_mean)/ train_std
temperature_model = gru_temperature_model(prev_values_count)
X_train = np.expand_dims(X_train, 2)
temperature_model.fit(X_train, y_train, epochs = 250, batch_size = 128)

X_test = np.expand_dims(X_test, 2)
y_test_predict = temperature_model.predict(X_test)

fig, ax = plt.subplots(1,1)
ax.plot(y_test.to_numpy(), label = "Actual values")
ax.plot(y_test_predict, label = "Predicted values")
plt.legend()
plt.show()

mae_test = np.sqrt(mean_absolute_error(y_test, y_test_predict))
print(f"Test set MAE:{mae_test}")

temperature_model.save(os.path.join(KERAS_MODEL_DIR,"temperature_pred_gru.h5"))
