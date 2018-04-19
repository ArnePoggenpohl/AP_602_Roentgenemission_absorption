import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

a, n = np.genfromtxt('abs_hg.txt', unpack=True)

x = a
y = n

plt.xlim(4,30)
# plt.ylim(-100,4000)
plt.plot(x, y, 'r-', linewidth=1, label='Messdaten')

plt.grid()

plt.ylabel(r'$\frac{\text{Impulse}}{\text{Sekunde}} \,/\, \frac{1}{s}$', fontsize=10)
plt.xlabel(r'Zählrohrwinkel $2 \theta \,/\, \si{\degree}$', fontsize=10)

plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)


plt.savefig('build/plot_abs_hg.pdf')
