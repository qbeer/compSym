import numpy as np
import matplotlib.pyplot as plt

# define theoretical function
def quadratic(x, a, b, c):
    return a*x**2 + b*x + c

quadratic = np.vectorize(quadratic)

# generating data with random noise

N = 500 # number of points
x = np.linspace(0, 50, N)
y_base = quadratic(x, 2, -3, 2)
y = np.multiply(np.random.choice(np.linspace(0.75, 1., 100), size=(N,)), y_base) # adding significant noise
err = np.multiply(np.random.choice(np.linspace(0.01, 0.05, 100), size=(N,)), y_base)

# visualizing original data
plt.subplot('121')
plt.title('Original data')
plt.errorbar(x, y, err, fmt='.', ecolor='r', elinewidth=1, label='f(x) = %.5f*x**2 + %.5f*x + %.5f' % (2, -3, 2))
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right')

# Least squares fitting for quadratic function
A = np.sum(y/np.square(err))
B = np.sum(np.dot(np.square(x), y)/np.square(err))
C = np.sum(np.dot(x, y)/np.square(err))

# quadratic terms
S = np.sum(1./np.square(err))
Sx = np.sum(x/np.square(err))
Sxx = np.sum(np.square(x)/np.square(err))
Sxxx = np.sum(np.dot(np.square(x), x)/np.square(err))
Sxxxx = np.sum(np.dot(np.square(x), np.square(x))/np.square(err))

D = np.array([[Sxx, Sx, S], [Sxxxx, Sxxx, Sxx], [Sxxx, Sxx, Sx]])
Dinv = np.linalg.inv(D)

params = np.matmul(Dinv, np.array([A, B, C]).T)

def fitted_quadratic(x, a, b, c):
    return a*x**2 +b*x +c

fitted_quadratic = np.vectorize(fitted_quadratic)

# visualizing the fit
plt.subplot('122')
plt.title('Fitted data')
plt.errorbar(x, y, err, fmt='.', ecolor='r', elinewidth=1, errorevery=5)
plt.plot(x, fitted_quadratic(x, params[0], params[1], params[2]), 'g.--',
 label='f(x) = %.5f*x**2 + %.5f*x + %.5f' % (params[0], params[1], params[2]))
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right')
plt.show()
