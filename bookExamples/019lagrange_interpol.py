energies = range(0, 201, 25)
data = [10.6, 16.0, 45.0, 83.5, 52.8, 19.9, 10.8, 8.25, 4.7]


def get_interpolated_function_value(x, values, measurements):
    lambdas = []
    for outer_ind in range(len(values)):
        lamb = 1.
        for inner_ind in range(0, outer_ind):
            lamb *= (x-values[inner_ind])/(values[outer_ind] - values[inner_ind])            
        for inner_ind in range(outer_ind+ 1, len(values)):
            lamb *= (x-values[inner_ind])/(values[outer_ind] - values[inner_ind])
        lambdas.append(lamb)
    sum = 0.
    for lamb, measurement in zip(lambdas, measurements):
        sum += lamb*measurement
    return sum

import matplotlib.pyplot as plt

plt.plot(energies, data, 'ro', label='Measured points')

rng = range(0, 201, 1)
scale = 1.

interpolated = [get_interpolated_function_value(x, energies, data) for x in rng]
max_interpolated = max(interpolated)
max_index = [i for i, j in enumerate(interpolated) if j == max_interpolated][0]
theoretical = [1./( (x - 78.)**2 + 55**2/4. ) for x in rng]
scale = interpolated[max_index]/theoretical[max_index]

plt.plot(rng, [get_interpolated_function_value(x, energies, data) for x in rng], 'b-', label='Lagrange interpolation')
plt.plot(rng, [scale*x for x in theoretical], 'g.--', label='Theory')
plt.legend(loc='upper right')
plt.show()
