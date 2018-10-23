import numpy as np

def random_walk(steps, initial_x, initial_y):
    path = [[initial_x, initial_y]]
    x = initial_x
    y = initial_y
    for step in range(steps):
        speed = 2 * np.random.random_sample((2, )) - 1.  # speed is random between [-1, 1]
        x += speed[0]
        y += speed[1]
        path.append([x, y])
    
    path = np.array(path)
    R2_actual = np.square(np.sum(np.diff(path[:, 0]))) + np.square(np.sum(np.diff(path[:, 1])))
    R2_expect = np.sum(np.square(np.diff(path[:, 0]))) + np.sum(np.square(np.diff(path[:, 1])))

    return path, np.sqrt(R2_actual), np.sqrt(R2_expect)

R2_actuals = []
R2_expects = []
paths = []
steps = np.linspace(100, 10000, 100).astype(int)

for N in steps:
    path, R2_actual, R2_expect = random_walk(N, 0., 0.)
    paths.append(path)
    R2_actuals.append(R2_actual)
    R2_expects.append(R2_expect)

import matplotlib.pyplot as plt

plt.figure(figsize=(15, 7))
plt.subplot("121")
plt.plot(np.sqrt(steps), R2_actuals, 'b.--', label='sqrt(R2 actual)')
plt.plot(np.sqrt(steps), R2_expects, 'r.--', label='sqrt(R2 expected value)')
plt.legend(loc='upper right')
plt.subplot("122")
plt.plot(paths[0][:, 0], paths[0][:, 1], 'g.--', label='First random path')
plt.plot(paths[49][:, 0], paths[49][:, 1], 'r.--', label='Fiftieth random path')
plt.plot(paths[99][:, 0], paths[99][:, 1], 'b.--', label='Hundredth random path')
plt.legend(loc='upper right')
plt.show()