import numpy as np

near_neighbor_corr = []

for N in range(1000, 50000, 1000):
    np_random = [np.random.random_sample() for i in range(0, N)]
    x = np.array(np_random[::2])
    y = np.array(np_random[1::2])

    near_neighbor_corr.append(np.dot(x, y)/x.size)

import matplotlib.pyplot as plt

plt.title('Near neighbor correlation')
plt.xlabel('Number of pairs')
plt.ylabel('Correlation function value')
plt.plot(range(500, 25000, 500), near_neighbor_corr, 'rx--')
plt.show()