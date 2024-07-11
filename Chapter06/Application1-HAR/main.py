import os.path as osp
from data_utils import read_data
from feature_utils import create_features
from sklearn import metrics
import sklearn2c
from matplotlib import pyplot as plt

DATA_PATH = osp.join("WISDM_ar_v1.1", "WISDM_ar_v1.1_raw.txt")
TIME_PERIODS = 80
STEP_DISTANCE = 40
data_df = read_data(DATA_PATH)
df_train = data_df[data_df["user"] <= 28]
df_test = data_df[data_df["user"] > 28]

train_segments_df, train_labels = create_features(df_train, TIME_PERIODS, STEP_DISTANCE)
test_segments_df, test_labels = create_features(df_test, TIME_PERIODS, STEP_DISTANCE)

bayes = sklearn2c.BayesClassifier()
bayes.train(train_segments_df, train_labels)
bayes_preds = bayes.predict(test_segments_df)

conf_matrix = metrics.confusion_matrix(test_labels, bayes_preds)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = conf_matrix, display_labels = bayes.class_names)
cm_display.plot()
cm_display.ax_.set_title("Bayes Classifier Confusion Matrix")
plt.show()

bayes.export("bayes_har_config")