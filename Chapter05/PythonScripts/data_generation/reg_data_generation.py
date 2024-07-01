import os.path as osp
import numpy as np

np.random.seed(42)  # For reproducibility

DATA_SIZE = 200
REGRESSION_DATA_DIR = "regression_data"

samples = np.array(range(DATA_SIZE)) / DATA_SIZE * 10
noise = np.random.normal(0, 0.5, DATA_SIZE)
line_values = 3 * samples + 4 + noise

noise = np.random.normal(0, 0.2, DATA_SIZE)
sine_values = np.sin(np.pi / 2 * samples) + noise

np.save(osp.join(REGRESSION_DATA_DIR, "reg_samples.npy"), np.expand_dims(samples, 1))
np.save(osp.join(REGRESSION_DATA_DIR,"reg_line_values.npy"), np.expand_dims(line_values, 1))
np.save(osp.join(REGRESSION_DATA_DIR, "reg_sine_values.npy"), np.expand_dims(sine_values, 1))