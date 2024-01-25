import os.path as osp
import numpy as np
from sklearn2c import SVMClassifier

train_samples = np.load(osp.join("classification_data", "cls_train_samples.npy"))
train_labels = np.load(osp.join("classification_data", "cls_train_labels.npy"))

svm = SVMClassifier()
model_save_path = osp.join("classification_models", "SVM_classifier.joblib")
svm.train(train_samples, train_labels, save_path= model_save_path)
