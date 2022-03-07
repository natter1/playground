from matplotlib import pyplot as plt


i = 0.001  # [A]
# r_u = 2000  # [Ohm] -> 1 mA ergibt max. 2 V (Schutz Multiplexer)

r_min = 10  # min R of measured resistor [Ohm]
r_max = 1000  # max R of measured resistor [Ohm]
u_limit = 2  # [V]
x = []  # zu messender Widerstand
u = []

def calc_voltages(r_list: list, r_u):  # voltage for given range, current, r_u ...
    result = []
    for r in r_list:
        r_ges = 1 / (1 / r_u + 1 / r)
        result.append(r_ges * i)
    return result

for r in range(r_min, r_max):
    x.append(r)

fig, ax = plt.subplots()

r_u_list = [10, 20, 100, 1000, 2000, 4000]
for r_u in r_u_list:
    ax.plot(x, calc_voltages(x, r_u), label=f"Ru = {r_u} Ohm")

ax.set_xlabel("R of single meander [Ohm]")
ax.set_ylabel(f"voltage over parallel resistors (I = {i*1000} mA)")
#ax.hlines(u_limit, x[0], x[-1], linestyles="dotted", label= "max voltage (multiplexer)")
ax.legend()
fig.show()

print(x)
