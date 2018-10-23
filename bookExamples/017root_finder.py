def poly(x):
    return 12*x**2 + x - 2

x_min = 0.
x_max = 12.
EPS = 1e-8

max_iter = 1000

for i in range(max_iter):
    bisection = ( x_max + x_min ) / 2.0
    y = poly(bisection)
    if y*poly(x_max) > 0.:
        x_max = bisection
    else:
        x_min = bisection
    if abs(y) < EPS:
        break

print("Loop ended at iteration %d with root value %.5f" % (i + 1, bisection))
