import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import *
from uncertainties import unumpy

Z, E = np.genfromtxt('rydberg.txt', unpack=True)

x = Z
y = np.sqrt(E*1000)

def f(x, A, B):
    return A*x+B

parameters, pcov = curve_fit(f, x, y)
errors = np.sqrt(np.diag(pcov))
print('A =',parameters[0], '±', errors[0])
print('B =',parameters[1], '±', errors[1])

z = np.linspace(32.5, 42.5, 100)
plt.plot(z, (f(z, *parameters)), 'r-', linewidth=1, label=r'Ausgleichsgrade')

plt.xlim(32.5, 42.5)
# plt.ylim(0, 5.3)

plt.plot(x, y , 'kx', label=r'Messdaten')
plt.ylabel(r' $\sqrt{E_\symup{K}} \,\, / \,\, $eV ', fontsize=10)
plt.xlabel(r'$ Z $', fontsize=10)

plt.legend(loc='best')
plt.grid()

plt.savefig('build/plot_rydberg.pdf')
