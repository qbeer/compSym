import numpy as np
import matplotlib.pyplot as plt

def rk4(t, Y_n, h, F):
    k1 = h*F(t, Y_n)
    k2 = h*F(t + h/2., Y_n + k1/2.)
    k3 = h*F(t + h/2., Y_n + k2/2.)
    k4 = h*F(t + h, Y_n + k3)
    return Y_n + (1./6.)*(k1 + 2*k2 + 2*k3 + k4)

# LVM
def F(t, Y_n):
    return LVM(np.array([Y_n[0], Y_n[1]]))

def LVM(Y):
    # general constants 
    eps = 0.15 # efficiency of hunting
    a = 0.75 
    b = 0.25 # might have to tune these
    m = 0.35
    return np.array([a*Y[0] - b*Y[0]*Y[1], eps*b*Y[0]*Y[1] - m*Y[1]])

y = [11.95, 2.15]
densities = []
for t in range(0, 1000):
    y = rk4(t, y, 0.095, F)
    densities.append(y)

densities = np.array(densities)
plt.plot(range(0, 1000), densities[:, 0], 'g.--', label='Prey')
plt.plot(range(0, 1000, 3), densities[:, 1][::3], 'r.--', label='Predators')
plt.legend(loc='upper right')
plt.show()
