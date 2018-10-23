N = 100
eps = 1.0

for i in range(0,N):
    eps /= 2.
    if (1.0 + eps) == 1.0:
        print('One plus eps : %.20f' % (1.0 + 2.*eps))
        print('One plus eps : %.20f' % (1.0 + eps))
        break

print('Machine precision is : %.20f' % eps)

# sinus function

def sin(x):
    n = 2
    sinx = x
    term = x
    term = -x**2/6. * term
    sinx = term + sinx
    quotient = term/sinx if term/sinx > 0. else -term/sinx
    while quotient > eps:
        n += 1
        term = -x**2/((2*n-1)*(2*n-2)) * term
        sinx = term + sinx
        quotient = term/sinx if term/sinx > 0. else -term/sinx
    return sinx

print(sin(1.))