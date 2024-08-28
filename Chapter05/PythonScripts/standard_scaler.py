import numpy as np
from sklearn.preprocessing import StandardScaler

np.random.seed(42)  # For reproducibility

def Gaussian2D(mean,L,theta,data_size):
    c, s = np.cos(theta), np.sin(theta)
    R = np.array([[c, -s], [s, c]])
    cov=R@L@R.T
    return np.random.multivariate_normal(mean, cov, data_size)

DATA_SIZE=1000
mean = [-2, -2]
E = np.diag([1,10])
theta=np.radians(45)
class1_samples = Gaussian2D(mean,E,theta,DATA_SIZE)

mean = [2, 2]
theta=np.radians(-45)
class2_samples = Gaussian2D(mean,E,theta,DATA_SIZE)

F=np.concatenate((class1_samples, class2_samples))
scaler = StandardScaler()
scaler = scaler.fit(F)
G=scaler.transform(F)