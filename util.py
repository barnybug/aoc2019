import numpy as np

def loadints(data):
    if isinstance(data, list):
        return np.array(data, dtype=int)
    return np.loadtxt(data, dtype=int)
