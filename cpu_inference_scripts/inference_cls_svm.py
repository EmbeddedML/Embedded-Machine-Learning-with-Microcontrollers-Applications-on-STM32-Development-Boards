import os.path as osp
import numpy as np
from sklearn2c import SVMClassifier


test_samples = np.load(osp.join("classification_data","cls_test_samples.npy"))
test_labels = np.load(osp.join("classification_data","cls_test_labels.npy"))

svm = SVMClassifier()
svm.load(osp.join("classification_models","SVM_classifier.joblib"))
preds = svm.inference(test_samples)
decisions = svm.clf.decision_function(test_samples)
print(test_samples[:5])
print(decisions[:5])
print(preds[:5])
