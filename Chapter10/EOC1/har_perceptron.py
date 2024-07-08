import os.path as osp
from data_utils import read_data
from feature_utils import create_features
from sklearn import metrics
import tensorflow as tf
from matplotlib import pyplot as plt

DATA_PATH = osp.join("WISDM_ar_v1.1", "WISDM_ar_v1.1_raw.txt")
TIME_PERIODS = 80
STEP_DISTANCE = 40
data_df = read_data(DATA_PATH)
df_train = data_df[data_df["user"] <= 28]
df_test = data_df[data_df["user"] > 28]

train_segments_df, train_labels = create_features(df_train, TIME_PERIODS, STEP_DISTANCE)
test_segments_df, test_labels = create_features(df_test, TIME_PERIODS, STEP_DISTANCE)

model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(1, input_shape = [10], activation = 'sigmoid')
  ])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=[tf.keras.metrics.BinaryAccuracy(),
                       tf.keras.metrics.FalseNegatives()])

train_segments_np = train_segments_df.to_numpy()
test_segments_np = test_segments_df.to_numpy()
train_labels[train_labels != "Walking"] = 1
train_labels[train_labels == "Walking"] = 0
test_labels[test_labels != "Walking"] = 1
test_labels[test_labels == "Walking"] = 0
train_labels = train_labels.astype(int)
test_labels = test_labels.astype(int)

model.fit(train_segments_np, train_labels, epochs=50, verbose=1)
perceptron_preds = model.predict(test_segments_np)

conf_matrix = metrics.confusion_matrix(test_labels, perceptron_preds > 0.5)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = conf_matrix, display_labels=["Walking", "Not Walking"])
cm_display.plot()
cm_display.ax_.set_title("Single Neuron Classifier Confusion Matrix")
plt.show()

model.save("har_neuron_model.h5")