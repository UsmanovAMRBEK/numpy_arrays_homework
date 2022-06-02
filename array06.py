import numpy as np

def main():
    """
    Create a 10x10 matrix, in which the elements on the borders will be equal to 1, and inside 0.

    """
    arr = np.zeros((10,10))
    arr[0, :] = arr[-1, :]= arr[:, 0] = arr[:, -1] = 1
    return arr
