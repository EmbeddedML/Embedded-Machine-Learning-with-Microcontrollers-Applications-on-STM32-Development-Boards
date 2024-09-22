import os
import numpy as np
from sklearn2c import SVMClassifier
from Data.paths import CLASSIFICATION_DATA_DIR
from Models.paths import CLASSIFICATION_MODEL_DIR

test_samples = np.load(os.path.join(CLASSIFICATION_DATA_DIR,"cls_test_samples.npy"))
test_labels = np.load(os.path.join(CLASSIFICATION_DATA_DIR,"cls_test_labels.npy"))

svc = SVMClassifier.load(os.path.join(CLASSIFICATION_MODEL_DIR, "svm_classifier.joblib"))
predictions = svc.predict(test_samples)
print(predictions)
