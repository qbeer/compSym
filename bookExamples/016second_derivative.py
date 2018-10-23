import numpy as np

derivs = []
ranges = []

for N in range(100, 1200, 100):
    values = np.linspace(0, 8*np.pi, N)
    ranges.append(values)
    step_size = values[1] - values[0]
    central_second_deriv = np.array([np.cos(x + step_size) + np.cos(x - step_size) - 2.*np.cos(x) for x in values])
    central_second_deriv /= step_size**2
    derivs.append(central_second_deriv)

derivs = np.array(derivs)

import matplotlib.pyplot as plt

for ind in range(derivs.shape[0]):
    plt.plot(ranges[ind],
        ind/derivs.shape[0] + np.abs(derivs[ind] - np.sin(ranges[ind]) + 10.) / (np.sin(ranges[ind]) + 10.),
        color=plt.cm.Set1(ind/derivs.shape[0]), marker='.')

plt.show()
