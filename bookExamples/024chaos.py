# logistic map
import numpy as np
import multiprocessing as mp
import matplotlib.pyplot as plt

output = mp.Queue()

def generate_pair(u, y):
    EPS = 1e-12
    lupanov = 0.0
    for i in range(0, 200):
        y = u*y*(1 - y)
        lupanov += np.log(np.abs(u - 2.*u*y) + EPS)
    return [u, y, lupanov/200.]

pool = mp.Pool(processes=4)
results = []

N = 500
mu = np.linspace(1, 4, N)
for u in mu:
    for x0 in np.linspace(0.0001, 0.9999, N//10 + 1):
        y = x0
        results.append(pool.apply_async(generate_pair, args=(u, y,)))
print('Processes started asynchronously!')

pairs = [p.get() for p in results]

pairs = np.array(pairs)
lupanov = pairs[:, 2]
pairs = pairs[:,0:2]

plt.subplot('121')
plt.scatter(pairs[:, 0][::5], pairs[:, 1][::5], marker='.', s=0.1, c=np.linalg.norm(pairs[::5], axis=1))

plt.subplot('122')
plt.plot(pairs[:, 0][::50], lupanov[::50], 'r.--')
plt.show()
