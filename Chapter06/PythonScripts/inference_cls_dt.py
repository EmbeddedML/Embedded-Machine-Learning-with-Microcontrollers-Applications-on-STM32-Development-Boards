import os
import numpy as np
from sklearn2c import DTClassifier

dirname = os.path.dirname

test_samples = np.load(os.path.join(dirname(__file__),"classification_data","cls_test_samples.npy"))
test_labels = np.load(os.path.join(dirname(__file__),"classification_data","cls_test_labels.npy"))

dtc = DTClassifier.load(os.path.join(dirname(__file__),"classification_models", "dt_classifier.joblib"))
predictions = dtc.predict(test_samples)
print(predictions)