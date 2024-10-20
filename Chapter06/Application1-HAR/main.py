import os
from sklearn import metrics
from matplotlib import pyplot as plt
import sklearn2c
from Data.paths import WISDM_PATH
from .data_utils import read_data
from .feature_utils import create_features
from Models.paths import CLASSIFICATION_MODEL_DIR, CLASSIFICATION_EXPORT_DIR

model_save_dir = os.path.join(CLASSIFICATION_MODEL_DIR, "har_bayes.joblib")
export_path = os.path.join(CLASSIFICATION_EXPORT_DIR, "har_bayes_config")
TIME_PERIODS = 80
STEP_DISTANCE = 40
data_df = read_data(WISDM_PATH)
df_train = data_df[data_df["user"] <= 28]
df_test = data_df[data_df["user"] > 28]

train_segments_df, train_labels = create_features(df_train, TIME_PERIODS, STEP_DISTANCE)
test_segments_df, test_labels = create_features(df_test, TIME_PERIODS, STEP_DISTANCE)

bayes = sklearn2c.BayesClassifier()
bayes.train(train_segments_df, train_labels, model_save_dir)
bayes_preds = bayes.predict(test_segments_df)
pred_class = bayes_preds.argmax(axis = 1)
pred_class_name = bayes.classes[pred_class]
conf_matrix = metrics.confusion_matrix(test_labels, pred_class_name)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = conf_matrix, display_labels = bayes.classes)
cm_display.plot()
cm_display.ax_.set_title("Bayes Classifier Confusion Matrix")
plt.show()

bayes.export(export_path)