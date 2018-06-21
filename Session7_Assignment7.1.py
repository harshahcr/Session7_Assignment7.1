import numpy as np
def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

a = np.array([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150])
moving_average(a)
mavg3 = moving_average(a, n=3)
print(mavg3)


mavg4 = moving_average(a, n=4)
print(mavg4)
