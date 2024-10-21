import os
import numpy as np
from sklearn2c import KNNClassifier
from Data.paths import CLASSIFICATION_DATA_DIR
from Models.paths import CLASSIFICATION_MODEL_DIR

test_samples = np.load(os.path.join(CLASSIFICATION_DATA_DIR,"cls_test_samples.npy"))
test_labels = np.load(os.path.join(CLASSIFICATION_DATA_DIR,"cls_test_labels.npy"))

knn = KNNClassifier.load(os.path.join(CLASSIFICATION_MODEL_DIR, "knn_classifier.joblib"))
predictions = knn.predict(test_samples)
print(predictions)