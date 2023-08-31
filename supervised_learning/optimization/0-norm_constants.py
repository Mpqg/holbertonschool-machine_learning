import numpy as np


def normalization_constants(X):
    """Calculate the mean and standard deviation."""
    # Calculate the mean and standard deviation along axis 0 (columns)
    means = np.mean(X, axis=0)
    std_devs = np.std(X, axis=0)
    return means, std_devs
