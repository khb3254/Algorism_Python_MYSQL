import numpy as np
def solution(array):
    array.sort()
    return np.median(array)