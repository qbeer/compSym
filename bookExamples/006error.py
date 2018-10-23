import numpy as np
import matplotlib.pyplot as plt

def log_error_terms(x, max_terms):
    sum = 0.
    zerothTerm = 1.
    nthTerm = zerothTerm
    sum += nthTerm
    values = []
    for term_ind in range(1, max_terms+1):
        nthTerm *= -x/term_ind
        sum += nthTerm
        values.append(sum)

    err = np.abs(np.exp(-x) - np.array(values)) / np.abs(np.exp(-x) + np.array(values))

    return np.linspace(1, max_terms, max_terms), err

for x in np.linspace(0., 1., 20):
    rng, err = log_error_terms(x, 20)
    plt.plot(rng, np.log(err), '.--', color=plt.cm.Set1(x), label='x = %.3f' % x)

plt.grid(True)
plt.legend(loc='upper right')
plt.show()