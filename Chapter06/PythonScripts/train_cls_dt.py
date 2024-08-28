import os
import numpy as np
from sklearn2c import DTClassifier

dirname = os.path.dirname

train_samples = np.load(os.path.join(dirname(__file__),"classification_data", "cls_train_samples.npy"))
train_labels = np.load(os.path.join(dirname(__file__),"classification_data", "cls_train_labels.npy"))

dtc = DTClassifier()
model_save_path = os.path.join(dirname(__file__),"classification_models", "dt_classifier.joblib")
dtc.train(train_samples, train_labels, save_path= model_save_path)