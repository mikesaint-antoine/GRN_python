import numpy as np
import simulation
import matplotlib.pyplot as plt
import sys


## TOGGLE SWITCH SSA
# simulation.toggle_switch_ssa(get_info=1)
# [G1,G2,t] = simulation.toggle_switch_ssa(plot_fig=1)

# f, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=False)
# line1, = ax1.plot(t , G1, color="b",label="G1")
# line2, = ax2.plot(t , G2, color="r",label="G2")
# ax1.set_ylabel('G1')
# ax2.set_ylabel('G2')

# ax2.set_xlabel('Time')
# plt.show()






## HILL ACTIVATION SSA
[G1,G2,t] = simulation.hill_activation_ssa(tend=50,plot_fig=1)



