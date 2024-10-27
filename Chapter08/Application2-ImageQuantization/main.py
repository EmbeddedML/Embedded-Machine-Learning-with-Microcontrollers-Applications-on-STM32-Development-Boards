import os
import cv2
from sklearn2c import Kmeans
from Data.paths import RGB_IMAGE_PATH
from Models.paths import CLUSTERING_MODEL_DIR, CLUSTERING_EXPORT_DIR

img = cv2.imread(RGB_IMAGE_PATH)

img_flat = img.reshape(-1,3)
kmeans = Kmeans()

kmeans.train(img_flat, os.path.join(CLUSTERING_MODEL_DIR, "rgb_quant_kmeans.joblib"))
kmeans.export(os.path.join(CLUSTERING_EXPORT_DIR,"rgb_quant_kmeans"))