import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


def u_to_p(x: float)-> float:
    return 10**((x-6.8)/0.6)


y = np.array([1000, 100, 10, 1, 0.1])
x = np.array([8.6, 8.0, 7.4, 6.8, 6.2])

popt, _ = curve_fit(lambda t, a, b: a + b**t, x, y)
result = curve_fit(lambda t, a: a**((t-6.8)/0.6), x, y)
print(popt)

plt.plot(x, y, 'bo', label='data')

x_fit = np.arange(0.01, 9, 0.01)
plt.plot(x_fit, u_to_p(x_fit), 'r-', label='fit')
plt.show()
