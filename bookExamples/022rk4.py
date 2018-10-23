# central potential, planet motion
# SI
import numpy as np

def rk4(t, Y_n, h, F):
    k1 = h*F(t, Y_n)
    k2 = h*F(t + h/2., Y_n + k1/2.)
    k3 = h*F(t + h/2., Y_n + k2/2.)
    k4 = h*F(t + h, Y_n + k3)
    return Y_n + (1./6.)*(k1 + 2*k2 + 2*k3 + k4)

# adaptive step size
def rk45(t, Y_n, h, F):
    EPS = 2.5
    Y_non_adaptive = rk4(t, Y_n, h, F)
    # double h until it exceeds the appropriate limit
    h = 2*h
    Y_adaptive = rk4(t, Y_n, h, F)
    temp = Y_adaptive
    while np.linalg.norm(Y_adaptive - Y_non_adaptive) < EPS:
        temp = Y_adaptive
        h = 2*h
        Y_adaptive = rk4(t, Y_n, h, F)
    return temp, h/2.

def euler(t, Y_n, h, F):
    return Y_n + h*F(t, Y_n)

# planetary motion
def F(t, Y_n):
    F = force(np.array([Y_n[0], Y_n[1]]))
    return np.array([Y_n[2], Y_n[3], F[0], F[1]])

def force(R):
    # general constants 
    G = 6.67408e-11
    M = 1.989e30
    return -G*M*R/np.linalg.norm(R)**3

R = [1.521e9, 0, 0, 29290] # start at the aphelion
R_e = R
h = .01
h_old = h
trajectory = []
euler_traj = []
N = 8e5
for t in np.linspace(0, N, N):
    #R = rk4(t, R, h, F)
    R, h_new = rk45(t, R, h, F)
    h = h_new
    R_e = euler(t, R_e, h_old, F)
    trajectory.append(R)
    euler_traj.append(R_e)

import matplotlib.pyplot as plt

trajectory = np.array(trajectory)
plt.plot(trajectory[:, 0][::25], trajectory[:, 1][::25], 'r--')
euler_traj = np.array(euler_traj)
plt.plot(euler_traj[:, 0][::25], euler_traj[:, 1][::25], 'g--')
plt.show()