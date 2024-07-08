import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import tensorflow as tf

np.random.seed(42)  # For reproducibility

def Gaussian2D(mean,L,theta,len):
	c, s = np.cos(theta), np.sin(theta)
	R = np.array([[c, -s], [s, c]])
	cov=R@L@R.T
	return np.random.multivariate_normal(mean, cov, len).T

len=1000
mean = [-2, -2]
E = np.diag([1,10])
theta=np.radians(45)
x1, y1 =Gaussian2D(mean,E,theta,len)

cls1=np.zeros((2,len))
cls1[0,:]=x1
cls1[1,:]=y1

len=1000
mean = [2, 2]
E = np.diag([1,10])
theta=np.radians(-45)
x2, y2 = Gaussian2D(mean,E,theta,len)

cls2=np.zeros((2,len))
cls2[0,:]=x2
cls2[1,:]=y2

F=np.concatenate((cls1,cls2),axis=1)
F=F.T

X=np.append(cls1, cls2, axis=1)
labels = np.hstack((np.zeros(len, dtype=np.uint8), np.ones(len, dtype=np.uint8)))
train_samples, test_samples, train_labels, test_labels = train_test_split(F, labels, test_size=0.2)

model = tf.keras.models.Sequential([
  tf.keras.layers.Dense(1, input_shape=[2], activation='sigmoid'),
  ])


model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
              loss=tf.keras.losses.BinaryCrossentropy(),
              metrics=[tf.keras.metrics.BinaryAccuracy(),
                       tf.keras.metrics.FalseNegatives()])
  

model.fit(train_samples, train_labels, validation_data = (test_samples, test_labels), epochs=50, verbose=1)
print("Finished training the model")