import os
import numpy as np
from sklearn.model_selection import train_test_split
from Data.paths import CLASSIFICATION_DATA_DIR

np.random.seed(42)  # For reproducibility
DATA_SIZE = 1000

def Gaussian2D(mean, L, theta, data_size):
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c, -s], [s, c]])
    cov = R @ L @ R.T
    return np.random.multivariate_normal(mean, cov, data_size)


mean = [-2, -2]
E = np.diag([1, 10])
theta = np.radians(45)

class1_samples = Gaussian2D(mean, E, theta, DATA_SIZE)

mean = [2, 2]
theta = np.radians(-45)

class2_samples = Gaussian2D(mean, E, theta, DATA_SIZE)
samples = np.concatenate([class1_samples, class2_samples])
labels = [0] * 1000 + [1] * 1000

train_samples, test_samples, train_labels, test_labels = train_test_split(
    samples, labels, test_size=0.2
)

np.save(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_samples.npy"), train_samples)
np.save(os.path.join(CLASSIFICATION_DATA_DIR, "cls_test_samples.npy"), test_samples)
np.save(os.path.join(CLASSIFICATION_DATA_DIR, "cls_train_labels.npy"), train_labels)
np.save(os.path.join(CLASSIFICATION_DATA_DIR, "cls_test_labels.npy"), test_labels)
