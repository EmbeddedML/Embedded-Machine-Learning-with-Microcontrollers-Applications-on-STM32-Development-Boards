import os
import cv2
from sklearn2c import Kmeans
from Data.paths import RGB_IMAGE_PATH
from Models.paths import CLUSTERING_EXPORT_DIR

img = cv2.imread(RGB_IMAGE_PATH)

img_flat = img.reshape(-1,3)
kmeans = Kmeans()

kmeans.train(img_flat)
kmeans.export(os.path.join(CLUSTERING_EXPORT_DIR,"rgb_quant_kmeans"))