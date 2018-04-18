import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

a, n = np.genfromtxt('data_4.txt', unpack=True)

x = a
y = n

# plt.xlim(0,70)
# plt.ylim(0,200)
plt.plot(x, y, 'rx', ms=3.5, label='Messdaten')

plt.grid()

plt.ylabel(r'$\frac{\text{Impulse}{\symup{s}}} \,/\, \frac{1}{s}$', fontsize=10)
plt.xlabel(r'$2 \theta \,/\, \si{\degree}$', fontsize=10)

plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)


plt.savefig('build/plot_emission.pdf')
