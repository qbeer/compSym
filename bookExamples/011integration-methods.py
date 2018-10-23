# OOP
import numpy as np


class Integrator:

    def __init__(self, func, a, b, number_of_steps):
        self.func = func
        self.a = a
        self.b = b
        self.number_of_steps = number_of_steps

    def trapezoid(self):
        step_size = (self.b - self.a) / (2.*(self.number_of_steps - 1))
        function_values = [self.func(
            self.a + delta) for delta in np.linspace(0, self.b - self.a, self.number_of_steps)]
        integral = 0.0
        for ind in range(len(function_values) - 1):
            integral += step_size*np.sum(function_values[ind:ind+2])
        return integral

    def simpson(self):
        step_size = (self.b - self.a) / (3*self.number_of_steps - 1)
        function_values = [self.func(
            self.a + delta) for delta in np.linspace(0, self.b - self.a, self.number_of_steps)]
        integral = 0.0
        for ind in range(0, len(function_values) - 2, 2):
            integral += step_size * \
                (np.sum(function_values[ind:ind+3]) + 3*function_values[ind+1])
        return integral

    def threeEights(self):
        step_size = 3.*(self.b - self.a) / (8.*self.number_of_steps - 1)
        function_values = [self.func(
            self.a + delta) for delta in np.linspace(0, self.b - self.a, self.number_of_steps)]
        integral = 0.0
        for ind in range(0, len(function_values) - 3, 3):
            integral += step_size * \
                (np.sum(function_values[ind:ind+4]) +
                 2*np.sum(function_values[ind+1:ind+3]))
        return integral

    def milne(self):
        step_size = (self.b - self.a) / (45.*self.number_of_steps - 1)
        function_values = [self.func(
            self.a + delta) for delta in np.linspace(0, self.b - self.a, self.number_of_steps)]
        integral = 0.0
        for ind in range(0, len(function_values) - 4, 4):
            integral += step_size * \
                (14*np.sum(function_values[ind:ind+5]) - 40. *
                 function_values[ind+2] + 50.*np.sum(function_values[ind+1:ind+4]))
        return integral


def expminusx2(x):
    return np.exp(-x**2)


integrator = Integrator(expminusx2, -100, 100, 10000)
print("Using 10000 steps and a range from -100 to 100 to integrate exp**(-x**2):")
print("\tTrapezoidal : %.7f" % integrator.trapezoid())
print("\tSimpson's   : %.7f" % integrator.simpson())
print("\tthreeEights : %.7f" % integrator.threeEights())
print("\tMilne       : %.7f" % integrator.milne())
print("\tActual val. : %.7f" % np.sqrt(np.pi))

def sin_poly(x):
    return np.sin(42.*x - 137.) * (x**3 - 7.*x**2 + 12*x - 137) 

integrals = []
rng = range(100, 5000, 200)
for N in rng:
    integrator = Integrator(sin_poly, -100, 100, N)
    integrals.append([integrator.trapezoid(), integrator.simpson(), integrator.threeEights(), integrator.milne()])

integrals = np.array(integrals)

import matplotlib.pyplot as plt

plt.plot(rng, integrals[:, 0], 'rx-', label='Trapezoid', markersize=11)
plt.plot(rng, integrals[:, 1], 'bo--', label='Simpson\'s')
plt.plot(rng, integrals[:, 2], 'g-', label='3/8')
plt.plot(rng, integrals[:, 3], 'c.--', label='Milne')
plt.title("Different integration methods on np.exp(-x**2)")
plt.xlabel("Number of steps")
plt.ylabel("Integral value")
plt.legend(loc='upper right')
plt.show()
