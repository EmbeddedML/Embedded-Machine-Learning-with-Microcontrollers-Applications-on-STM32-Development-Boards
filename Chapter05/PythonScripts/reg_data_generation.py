import os
import numpy as np
from Data.paths import REGRESSION_DATA_DIR

np.random.seed(42)  # For reproducibility

DATA_SIZE = 200

# Generate noisy line data
samples = np.array(range(DATA_SIZE)) / DATA_SIZE * 10
samples = np.expand_dims(samples, axis = 1) #Alternatively, np.reshape(samples, (DATA_SIZE, 1))
noise = np.random.normal(0, 0.5, (DATA_SIZE, 1))
line_values = 3 * samples + 4 + noise

# Generate noisy sine data
noise = np.random.normal(0, 0.2, (DATA_SIZE, 1))
sine_values = np.sin(np.pi / 2 * samples) + noise

np.save(os.path.join(REGRESSION_DATA_DIR, "reg_samples.npy"), samples)
np.save(os.path.join(REGRESSION_DATA_DIR, "reg_line_values.npy"), line_values)
np.save(os.path.join(REGRESSION_DATA_DIR, "reg_sine_values.npy"), sine_values)
