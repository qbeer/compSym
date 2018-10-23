import numpy as np
import matplotlib.pyplot as plt

N = 400
T = 50 # sampling time
t = np.linspace(0, T, N)
Z = np.exp(complex(0, 2.*np.pi/N))

def xplussinx(t, T):
    # T/2 periodicity, T is sampling time
    if t > T/2.:
        return 0.05*np.random.random_sample()*np.sin( (t - T/2.) ) + ( t -T/2.) / (T/2.)
    else:
        return 0.05*np.random.random_sample()*np.sin(t) + 2.*t/T

xplussinx = np.vectorize(xplussinx)
y = xplussinx(t, T)

plt.subplot('231')
plt.plot(t, y, 'r.--', label='f(t)')
plt.legend(loc='upper right')

# DFT
Zn = [Z**n for n in range(0, N + 1)]
Z = np.zeros(shape=(N+1, N), dtype=np.complex_)
for row in range(N + 1):
    for col in range(N):
        Z[row, col] = Zn[row]**(col + 1)

Y = np.matmul(Z, y.T)/np.sqrt(2.*np.pi)
y_new = np.sqrt(2.*np.pi)*np.matmul(1./Z.T, Y)/N

plt.subplot('232')
plt.plot(t, y_new.real, 'g.--')

plt.subplot('233')
plt.plot(Y.real, Y.imag, 'b.')

# noise reduction
# consider that the sinus is noise on the data

def xplussinxAuto(tau, x, T):
    return np.multiply(xplussinx(x, T), xplussinx(tau + x, T)) # vecotorized

print("Calculating auto correlation...")

auto = []
step_size = t[1] - t[0]
for tau in np.linspace(-T, T, N):
    current_func = xplussinxAuto(tau, t, T)
    auto.append(np.array(current_func)*step_size)

print("Fourier transform of AC...")

Z = np.exp(complex(0, 2.*np.pi/N))

# DFT on the auto correlation
auto = np.array(auto)
auto = np.mean(auto, axis=0)
M = auto.shape[0]
Zn = [Z**n for n in range(0, M + 1)]
Z = np.zeros(shape=(M+1, M), dtype=np.complex_)
for row in range(M + 1):
    for col in range(M):
        Z[row, col] = Zn[row]**(col + 1)

Y = np.matmul(Z, auto.T)/np.sqrt(2.*np.pi)
power = np.square([np.absolute(y) for y in Y])

plt.subplot('234')
plt.plot(np.linspace(0, T, N), auto, 'r.--')


plt.subplot('235')
plt.plot(power, 'ro')
plt.xlim(0,15)
plt.ylim(0, 40)

# low pass filter
omega = np.linspace(0, 2*np.pi/T, N + 1)
fourier_filter = 1./(1. + complex(0., 1.)*omega*5)
Y = np.multiply(Y, fourier_filter.T)*np.sqrt(np.pi*2)
y_new = np.sqrt(2.*np.pi)*np.matmul(1./Z.T, Y)/M

plt.subplot('236')
plt.plot(y_new.real, 'r.--')
plt.show()
