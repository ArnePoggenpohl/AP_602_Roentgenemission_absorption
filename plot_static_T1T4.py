import matplotlib.pyplot as plt
import numpy as np

a, T1, T2, T3, T4, T5, T6, T7, T8 = np.genfromtxt('data_static.txt', unpack=True)

x = a/5

plt.plot(x, T1, 'r-', label=r'$Messing_{breit}$')
plt.plot(x, T4, 'b-', label=r'$Messing_{schmal}$')
plt.xlabel('t[$s$]')
plt.ylabel('T[$°C$]')
plt.legend(loc='best')
plt.grid()

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot_static_T1T4.pdf')
