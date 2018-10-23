import matplotlib.pyplot as plt
import numpy as np

S_up = 0.
S_down = 0.

ups = []
downs = []

N = 50000

for i in range(1, N + 1):
    S_up += 1./i
    ups.append(S_up)
    
    S_down += 1./(N + 1 - i)
    downs.append(S_down)

plt.plot(range(1, N+1), ups, 'b.--', label='S_up')
plt.plot(range(1, N+1), downs, 'r.--', label='S_down')
plt.xlabel('Number of points')
plt.ylabel('Series value')
plt.legend()
plt.show()

err = np.array(ups) - np.array(downs)
err /= (np.abs(np.array(ups)) + np.abs(np.array(downs)))
plt.plot(np.log(range(1, N+1)), np.log(err), 'g.--', label='Error')
plt.xlabel('log(N)')
plt.ylabel('log(rel_err)')
plt.show()