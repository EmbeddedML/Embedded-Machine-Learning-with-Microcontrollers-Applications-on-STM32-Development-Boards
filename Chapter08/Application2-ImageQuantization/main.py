import cv2
from sklearn2c import Kmeans

img = cv2.imread("im_rgb.jpg")

img_flat = img.reshape(-1,3)
kmeans = Kmeans()

kmeans.train(img_flat)
kmeans.export("image_quantization")