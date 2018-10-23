import numpy as np

def integrate(steps, fr=-100., to=100.):
    x = np.linspace(fr, to, steps)
    values = np.exp(-np.square(x))*(to - fr)/steps
    return np.sum(values)

integral_values = []

N = 500000

for steps in range(1000, N, 1000):
    integral_values.append(integrate(steps))

err = np.abs(np.sqrt(np.pi) - np.array(integral_values))
err /= (np.sqrt(np.pi))

import matplotlib.pyplot as plt

plt.plot(range(1000, N, 1000), np.log(err), 'b.--')
plt.show()