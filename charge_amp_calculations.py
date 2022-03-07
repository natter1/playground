import numpy as np
from matplotlib import pyplot as plt

q_in = 16e-12  # [C] (16 pC)  - Schätzung aus 1,6V Signal (mV/pC) bei 100x Verstärkung (Anregung 1V)
c_min = 5e-12  # [F]
c_max = 20e-12  # [F]

def calc_voltages(c_list: list, q_in):
    result = []
    for c_f in c_list:
        u_c = q_in / c_f
        result.append(u_c)
    return result


x = []  # capacity for charge amplifier (RC
for c in np.linspace(c_min, c_max, 100):
    x.append(c)

u = []


fig, ax = plt.subplots()


ax.plot( [value * 1e12 for value in x], calc_voltages(x, q_in), label=f"q_in = {q_in*1e12} pC")

ax.set_xlabel("c_f [pF]")
ax.set_ylabel(f"voltage signal [V]")
#ax.hlines(u_limit, x[0], x[-1], linestyles="dotted", label= "max voltage (multiplexer)")
ax.legend()
fig.show()


# --------------------------------------
# calc fu
# --------------------------------------
def calc_frequencies(x: list, cf):
    result = []
    for r_value in x:
        fu = 1 / (2*np.pi * r_value * cf)
        result.append(fu)
    return result



cf_list = [10e-12, 100e-12, 1000e-12]
r_min = 1e10
r_max = 1e12
x = []  # Ohm

for r in np.linspace(r_min, r_max, 100):
    x.append(r)

fig, ax = plt.subplots()

for cf in cf_list:
    ax.plot([value * 1 for value in x], calc_frequencies(x, cf), label=f"cf = {cf*1e12} pF")

ax.set_xlabel("R [Ohm]")
ax.set_ylabel(f"freq.")
#ax.hlines(u_limit, x[0], x[-1], linestyles="dotted", label= "max voltage (multiplexer)")
ax.legend()
fig.show()
