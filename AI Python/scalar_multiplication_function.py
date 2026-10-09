import numpy as np

def scale_vector(vector, scalar):
    return scalar * vector

print(scale_vector(np.array([3,-5]), -2))