import numpy as np

def random_gen(val, a, b, M):
    return (a*val + b) % M

my_random = []
numpy_random = []
seed = 4200

for i in range(0, 10000):
    seed = random_gen(seed, 1321, 137, 1923)
    my_random.append(seed)
    numpy_random.append(np.random.random_sample())

import matplotlib.pyplot as plt

plt.figure(figsize=(15, 7))

plt.subplot("121")
plt.plot(my_random[1::2], my_random[::2], 'bx')
plt.title("Generated random sample by 'bad' generator")
plt.xlabel('x')
plt.ylabel('y')

plt.subplot("122")
plt.title("Generated random sample by 'good' generator")
plt.plot(numpy_random[1::2], numpy_random[::2], 'bx')
plt.xlabel('x')
plt.ylabel('y')

plt.show()