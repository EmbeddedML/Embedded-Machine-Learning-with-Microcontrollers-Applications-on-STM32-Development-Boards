import os
import numpy as np
from sklearn2c import KNNClassifier

dirname = os.path.dirname

test_samples = np.load(os.path.join(dirname(__file__),"classification_data","cls_test_samples.npy"))
test_labels = np.load(os.path.join(dirname(__file__),"classification_data","cls_test_labels.npy"))

knn = KNNClassifier.load(os.path.join(dirname(__file__),"classification_models", "knn_classifier.joblib"))
predictions = knn.predict(test_samples)
print(predictions)