import numpy as np
import simulation
import matplotlib.pyplot as plt
import sys





[G1,G2,t] = simulation.toggle_switch_ssa(plot_fig=1)


print(len(G1))
print(len(G2))
print(len(t))


# f, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=False)
# line1, = ax1.plot(t , G1, color="b",label="G1")
# line2, = ax2.plot(t , G2, color="r",label="G2")
# ax1.set_ylabel('G1')
# ax2.set_ylabel('G2')

# ax2.set_xlabel('Time')
# plt.show()