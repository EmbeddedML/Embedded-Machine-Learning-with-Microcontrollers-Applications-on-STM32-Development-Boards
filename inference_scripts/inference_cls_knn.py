import os.path as osp
import numpy as np
from sklearn2c import KNNClassifier

test_samples = np.load(osp.join("classification_data","cls_test_samples.npy"))
test_labels = np.load(osp.join("classification_data","cls_test_labels.npy"))

knn = KNNClassifier.load(osp.join("classification_models", "KNN_classifier.joblib"))
predictions = knn.inference(test_samples)
print(predictions)