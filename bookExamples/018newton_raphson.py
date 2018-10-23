import numpy as np


def poly(x):
    return x**4 + 12*x**3 - 2*x + 136.

def poly_deriv(x):
    delta = 1e-9
    return ( poly(x + delta) - poly(x) ) / delta

x = -3.
max_iter = 1000
EPS = 1e-12 # zero tolerance

for i in range(max_iter):
    if abs(poly(x)) < EPS:
        break
    x = x - poly(x)/poly_deriv(x)

print('Root found at iteration %d at value %.15f' % (i + 1, x))

print('\n*****************************************************\n')

def hard_func(x):
    return np.sin(x) * x
def hard_func_deriv(x):
    delta = 1e-9
    return ( hard_func(x + delta) - hard_func(x) ) / delta

# poll the function to find intervals
rng = np.linspace(-10, 10, 1000)
polled_func = [hard_func(x) for x in rng] # find +/- changes
polled_func_deriv = [hard_func_deriv(x) for x in rng] # to find minimum exactly at zero, touching the y-axis

def signum(x):
    return 1 if x >= 0. else -1
intervals = []
polled_func = [signum(x) for x in polled_func]
polled_func_deriv = [signum(x) for x in polled_func_deriv]

for ind in range(len(polled_func) - 1):
    if polled_func[ind]*polled_func[ind + 1] < 0.:
        intervals.append([rng[ind - 5], rng[ind + 5]])

for interval in intervals:
    x = interval[1] # end of the interval
    for i in range(max_iter):
        if abs(hard_func(x)) < EPS:
            break
        x = x - hard_func(x)/hard_func_deriv(x)
    print('Root found at iteration %d at value %.15f' % (i + 1, x))