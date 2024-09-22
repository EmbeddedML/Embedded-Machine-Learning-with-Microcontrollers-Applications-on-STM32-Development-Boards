import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from matplotlib import pyplot as plt
import tensorflow as tf

df = pd.read_csv("temperature_dataset.csv")
y = df["Room_Temp"][::4]
prev_values_count = 5

X = pd.DataFrame()
for i in range(prev_values_count, 0, -1):
    X["t-" + str(i)] = y.shift(i)

X = X[prev_values_count:]
y = y[prev_values_count:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

train_mean = X_train.mean()
train_std = X_train.std()

X_train = (X_train - train_mean) / train_std
X_test = (X_test - train_mean) / train_std

model = tf.keras.models.Sequential([tf.keras.layers.Dense(1, input_shape=[5])])

model.compile(
    optimizer=tf.keras.optimizers.SGD(learning_rate=5e-3),
    loss=tf.keras.losses.MeanAbsoluteError(),
)

model.fit(
    X_train,
    y_train,
    batch_size=128,
    epochs=3000,
    verbose=1,
    workers=16,
    use_multiprocessing=True,
)

y_train_predicted = model.predict(X_train)
y_test_predict = model.predict(X_test)

fig, ax = plt.subplots(1,1)
ax.plot(y_test.to_numpy(), label = "Actual values")
ax.plot(y_test_predict, label = "Predicted values")
plt.legend()
plt.show()

mae_train = np.sqrt(mean_absolute_error(y_train, y_train_predicted))
mae_test = np.sqrt(mean_absolute_error(y_test, y_test_predict))

print(f"Training set MAE: {mae_train}\n")
print(f"Test set MAE:{mae_test}")

model.save("temperature_prediction_perceptron.h5")