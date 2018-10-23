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

    def gaussian(self):
        x, w = self.get_weights(self.a, self.b, self.number_of_steps)
        return np.dot(np.array([self.func(val) for val in x]), w)

    def get_weights(self, a, b, N):
        EPS = 10**-12
        m = (N + 1.) / 2.
        xm = 0.5*(a+b)
        xl = 0.5*(b-a)
        x = [0]*N
        w = [0]*N
        for i in range(np.array(m).astype(int)):
            z = np.cos(np.pi*(i+0.75)/(N+0.5))
            z1 = 2*z # random initialization, does not matter
            while np.abs(z-z1) > EPS:
                p1 = 1.0
                p2 = 0.0
                for j in range(N):
                    p3 = p2
                    p2 = p1
                    p1 = ((2.0 * j + 1.0)*z*p2-j*p3)/(j+1)
                pp = N*(z*p1-p2)/(z*z-1.0)
                z1 = z
                z = z1 - p1/pp
            x[i] = xm - xl*z
            x[N-1-i] = xm+xl*z
            w[i] = 2.0*xl/((1.0-z*z)*pp*pp)
            w[N-1-i] = w[i]
        return x, w

def poly(x):
    return x**3 - 7.*x**2 + 12*x - 137

integrals = []
rng = range(100, 1500, 100)
for N in rng:
    integrator = Integrator(poly, 0, 12, N)
    integrals.append([integrator.trapezoid(), integrator.simpson(), integrator.gaussian()])

integrals = np.array(integrals)

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 5))
plt.subplot("121")
plt.plot(rng, integrals[:, 0], 'rx-', label='Trapezoid', markersize=11)
plt.plot(rng, integrals[:, 2], 'g-', label='Gaussian')
plt.title("Different integration methods on x**3 - 7*x**2 + 12*x + 137")
plt.xlabel("Number of steps")
plt.ylabel("Integral value")
plt.legend(loc='upper right')

error0 = np.abs((integrals[:, 0] - 372) / integrals[:, 0])
error1 = np.abs((integrals[:, 1] - 372) / integrals[:, 1])
error2 = np.abs((integrals[:, 2] - 372) / integrals[:, 2])

plt.subplot("122")
plt.plot(rng, error0, 'rx-', label='Trapezoid', markersize=11)
#plt.plot(rng, error1, 'b.--', label='Simpson\'s')
plt.plot(rng, error2, 'g-', label='Gaussian')
plt.title("Error of different integration methods on x**3 - 7*x**2 + 12*x + 137")
plt.xlabel("Number of steps")
plt.ylabel("|error|")
plt.legend(loc='upper right')

plt.show()
