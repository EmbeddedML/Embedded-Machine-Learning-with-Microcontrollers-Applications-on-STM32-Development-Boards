import os
import numpy as np
import keras
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from matplotlib import pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from .data_utils import read_data
from .feature_utils import create_features
from Data.paths import WISDM_PATH
from Models.paths import KERAS_MODEL_DIR

TIME_PERIODS = 80
STEP_DISTANCE = 40
data_df = read_data(WISDM_PATH)
df_train = data_df[data_df["user"] <= 28]
df_test = data_df[data_df["user"] > 28]

train_segments_df, train_labels = create_features(df_train, TIME_PERIODS, STEP_DISTANCE)
test_segments_df, test_labels = create_features(df_test, TIME_PERIODS, STEP_DISTANCE)

model = keras.models.Sequential([
  keras.layers.Dense(100, input_shape=[10], activation="relu"),
  keras.layers.Dense(100, activation="relu"),
  keras.layers.Dense(6, activation = "softmax")
  ])

train_segments_np = train_segments_df.to_numpy()
test_segments_np = test_segments_df.to_numpy()
ohe = OneHotEncoder()
train_labels_ohe = ohe.fit_transform(train_labels.reshape(-1, 1)).toarray()
categories, test_labels = np.unique(test_labels, return_inverse = True)
model.compile(loss=keras.losses.CategoricalCrossentropy(), optimizer=keras.optimizers.Adam(1e-3))
model.fit(train_segments_np, train_labels_ohe, epochs=50, verbose = 1)
nn_preds = model.predict(test_segments_np)
predicted_classes = np.argmax(nn_preds, axis = 1)

conf_matrix = confusion_matrix(test_labels, predicted_classes)
cm_display = ConfusionMatrixDisplay(confusion_matrix = conf_matrix, display_labels= categories)
cm_display.plot()
cm_display.ax_.set_title("Neural Network Confusion Matrix")
plt.show()

model.save(os.path.join(KERAS_MODEL_DIR,"har_mlp.h5"))