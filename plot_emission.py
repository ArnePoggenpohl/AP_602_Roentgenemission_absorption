import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

a, n = np.genfromtxt('Emissionsspektrum.txt', unpack=True)

fig = plt.figure()
ax = fig.add_subplot(111)
x = a
y = n

plt.xlim(8,52)
plt.ylim(-100,4000)
plt.plot(x, y, 'r-', linewidth=1, label='Messdaten')

ax.annotate(r'$K_{\beta}$', xy=(39.6, 1070), xytext=(31.8, 1175),
            arrowprops=dict(facecolor='black', shrink=0.1))

ax.annotate(r'$K_{\alpha}$', xy=(44.7, 3800), xytext=(36.8, 3175),
            arrowprops=dict(facecolor='black', shrink=0.1))

ax.annotate(r'Bremsberg', xy=(23, 250), xytext=(13, 675),
            arrowprops=dict(facecolor='black', shrink=0.1))


plt.grid()

plt.ylabel(r'$\text{Impulse} \,/\, \frac{1}{s}$', fontsize=10)
plt.xlabel(r'Zählrohrwinkel $2 \theta \,/\, \si{\degree}$', fontsize=10)

plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)


plt.savefig('build/plot_emission.pdf')
