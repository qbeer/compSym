import numpy as np

def weight_func(x):
    # from -1 to 1 distribution
    return np.exp(-np.log((1+x)/(1-x))**2/8.)/(np.sqrt(2.*np.pi)*(1-x**2))

random_points = [2.*np.random.random_sample((2,)) - 1. for i in range(0, 10000)]
random_points_distributed = list(filter(lambda point: point[1] < weight_func(point[0]), random_points))

import matplotlib.pyplot as plt

plt.subplot('121')
plt.plot(random_points, 'b.')

plt.subplot('122')
plt.plot(random_points_distributed, 'r.')

plt.show()
