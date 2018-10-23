import numpy as np
import matplotlib.pyplot as plt

A = [0., 0.]
B = [5., np.sqrt(3)*5.]
C = [10., 0.]

vertices = [A, B, C]

plt.plot(A[0], A[1], 'b.')
plt.plot(B[0], B[1], 'b.')
plt.plot(C[0], C[1], 'b.')

P = [3., 4.]

plt.plot(P[0], P[1], 'r.')

for n in range(0, 5000):
    r = np.random.random_sample()
    n = np.around(2*r).astype(int)
    x = vertices[n][0] + P[0]
    y = vertices[n][1] + P[1]
    x /= 2
    y /= 2
    P = [x, y]
    plt.plot(x, y, 'g.')

plt.show()