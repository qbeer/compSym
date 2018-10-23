import numpy as np
import matplotlib.pyplot as plt

def poly(x):
    return x**4 - 8*x**2


N = 50
x = np.linspace(-2, 2, N)
step_size = x[1] - x[0]
forward_step = []
central_step = []

for ind in range(N-1):
    forward_step.append((poly(x[ind + 1]) - poly(x[ind]))/step_size)

for ind in range(N):
    central_step.append((poly(x[ind] + step_size/2.) - poly(x[ind] - step_size/2.))/step_size)

plt.subplot("121")
plt.plot(x, [poly(value) for value in x], 'bo--', label='Function')
plt.plot(x[:x.shape[0]-1], forward_step, 'g.--', label='Forward step derivative')
plt.plot(x, central_step, 'rx--', label='Central step derivative')
plt.plot(x, [4*value**3 - 16*value for value in x], label='Analytic derivative')
plt.legend(loc='upper right')


err0 = np.abs(np.array(forward_step) - np.array([4*value**3 - 16*value for value in x])[:x.shape[0]-1])
err0 /= np.array([4*value**3 - 16*value for value in x])[:x.shape[0]-1]

err1 = np.abs(np.array(central_step) - np.array([4*value**3 - 16*value for value in x]))
err1 /= np.array([4*value**3 - 16*value for value in x])

plt.subplot("122")
plt.plot(err0, label='Forward step error')
plt.plot(err1, label='Central step error')
plt.legend(loc='upper right')
plt.show()