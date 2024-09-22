import numpy as np

def load_images(path):
    with open(path, "rb") as f:
        buffer = f.read()[16:]
        images = np.frombuffer(buffer, dtype=np.uint8).reshape(-1, 28, 28)
    return images

def load_labels(path):
    with open(path, "rb") as f:
        buffer = f.read()[8:]
        labels = np.frombuffer(buffer, dtype=np.uint8)
    return labels