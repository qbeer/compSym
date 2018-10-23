import numpy as np

areas = []

for N in range(1000, 10000, 100):
    stones = range(1000) # throw N stones
    thrown_stones = len(stones)
    caught_stones = 0
    for stone in stones:
        x, y = 2. * np.random.random_sample((2, )) - 1.
        if x**2 + y**2 < 1.:
            caught_stones += 1
    areas.append(4.*caught_stones/thrown_stones)

import matplotlib.pyplot as plt

plt.plot(range(1000, 10000, 100), areas, 'b.-', label="Area")
plt.plot(range(1000, 10000, 100), [np.pi for area in areas], 'r-', label='Expected value')
plt.legend(loc='upper right')
plt.xlabel("Number of stones")
plt.ylabel("Area")
plt.show()

# 10D integral (x1 + x2 + x3 + x4 + ... + x10)**2 from 0 to 1 for each
# avg of random values times the bounding size (which is one now)
function_values = []
for i in range(100000):
    x = np.random.random_sample((10,))
    function_values.append(np.square(np.sum(x)))
print("The value of the multi dim integral is: %.5f and it should be %.5f" % (np.mean(function_values), 155./6.))

mean_values = []
for i in range(0, 99900, 100):
    mean_values.append(np.mean(function_values[0:i+100]))
err = np.abs(np.array(mean_values) - 155./6.)
err /= (155./6.)

plt.plot(1./np.sqrt(range(100, 100000, 100)), err, 'b.--', label='Error')
plt.show()
