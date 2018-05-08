import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

a, n = np.genfromtxt('Bragg.txt', unpack=True)

x = a
y = n

plt.xlim(26,30)
# plt.ylim(-100,4000)
plt.plot(x, y, 'r-', linewidth=1, label='Messdaten')

plt.grid()

plt.ylabel(r'$\text{Impulse} \,/\, \frac{1}{s}$', fontsize=10)
plt.xlabel(r'Zählrohrwinkel $2 \theta \,/\, \si{\degree}$', fontsize=10)

plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)


plt.savefig('build/plot_bragg.pdf')
