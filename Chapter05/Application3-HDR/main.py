import os 
from .mnist import load_images, load_labels
import numpy as np
import cv2
from Data.paths import MNIST_PATH

train_img_path = os.path.join(MNIST_PATH, "train-images.idx3-ubyte")
train_label_path = os.path.join(MNIST_PATH, "train-labels.idx1-ubyte")
test_img_path = os.path.join(MNIST_PATH, "t10k-images.idx3-ubyte")
test_label_path = os.path.join(MNIST_PATH, "t10k-labels.idx1-ubyte")

train_images = load_images(train_img_path)
train_labels = load_labels(train_label_path)
test_images = load_images(test_img_path)
test_labels = load_labels(test_label_path)

train_huMoments = np.empty((len(train_images),7))
test_huMoments = np.empty((len(test_images),7))

for train_idx, train_img in enumerate(train_images):
    train_moments = cv2.moments(train_img, True) 
    train_huMoments[train_idx] = cv2.HuMoments(train_moments).reshape(7)

for test_idx, test_img in enumerate(test_images):
    test_moments = cv2.moments(test_img, True) 
    test_huMoments[test_idx] = cv2.HuMoments(test_moments).reshape(7)