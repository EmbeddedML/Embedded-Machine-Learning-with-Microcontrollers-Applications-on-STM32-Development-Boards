import os.path as osp
import numpy as np
from sklearn2c import SVMClassifier

test_samples = np.load(osp.join("classification_data","cls_test_samples.npy"))
test_labels = np.load(osp.join("classification_data","cls_test_labels.npy"))

svc = SVMClassifier.load(osp.join("classification_models", "SVM_classifier.joblib"))
predictions = svc.predict(test_samples)
print(predictions)
