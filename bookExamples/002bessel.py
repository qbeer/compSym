import numpy as np

def j0(x):
    return np.sin(x)/x

def j1(x):
    return np.sin(x)/x**2 - np.cos(x)/x

def up(x, l):
    j = np.zeros(l+1)
    j[0] = j0(x)
    j[1] = j1(x)
    for ind in range(1, l):
        print(ind, ' .')
        j[ind+1] = (2.*ind+1.)*j[ind]/x - j[ind-1]
    return np.sum(j)

print("j%d(%.5f) = %.5f" % (3, 0.1, up(0.1, 3)))


