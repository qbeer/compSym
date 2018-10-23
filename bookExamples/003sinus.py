def sin(x, eps):
    if x == 0:
        return 0
    firstTerm = x
    nthTerm = firstTerm
    sum = firstTerm
    N = 1
    error = nthTerm/sum
    error = error if error > 0 else -error
    while eps < error:
        nthTerm = -nthTerm*x**2/(4*N**2 + 2*N)
        sum += nthTerm
        N += 1
        error = nthTerm/sum
        error = error if error > 0 else -error
    return sum

eps = 0.0000000000000002 # required by adding it to 1.

print('sin(%.3f) = %.15f' % (0., sin(0., eps)))
print('sin(%.3f) = %.15f' % (3.14159, sin(3.14159, eps)))
print('sin(%.3f) = %.15f' % (1.57, sin(1.57, eps)))