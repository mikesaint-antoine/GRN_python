import numpy as np
import matplotlib.pyplot as plt
import random
import sys



def toggle_switch_ssa(get_info=0,tend=1000, params=[1, 0.2, 1, 0.2, 1, 9],init=[0,0],plot_fig=0):
    # params: [k_1, gamma_1, k_2, gamma_2, c, h]

    if get_info:
        print()
        print("TOGGLE SWITCH SSA MODEL")
        print("params: [k_1, gamma_1, k_2, gamma_2, c, h]")
        # print("default: [1, 0.2, 1, 0.2, 1, 9]")
        print(f"default: {params}")

        return()





    G1 = [init[0]]
    G2 = [init[1]]
    t = [0]


    k_1 = params[0]
    gamma_1 = params[1]
    k_2 = params[2]
    gamma_2 = params[3]


    c = params[4]
    h = params[5]


    while t[-1] < tend:

        props = [(c**h / (c**h + G2[-1]**h)) * k_1, gamma_1 * G1[-1], \
        (c**h / (c**h + G1[-1]**h)) * k_2, gamma_2 * G2[-1]]


        prop_sum = sum(props)


        tau = np.random.exponential(scale=1/prop_sum)

        t.append(t[-1] + tau)


        rand = random.uniform(0,1)


        # G1 production event
        if rand * prop_sum <= props[0]:
                G1.append(G1[-1] + 1)
                G2.append(G2[-1])

        # G1 decay event
        elif rand * prop_sum > props[0] and rand * prop_sum <= sum(props[:2]):
                G1.append(G1[-1] - 1)
                G2.append(G2[-1])

        # G2 production event
        elif rand * prop_sum > sum(props[:2]) and rand * prop_sum <= sum(props[:3]):
                G1.append(G1[-1])
                G2.append(G2[-1] + 1)

        # G2 decay event
        elif rand * prop_sum > sum(props[:3]) and rand * prop_sum <= sum(props[:4]):
                G1.append(G1[-1])
                G2.append(G2[-1] - 1)    

    # cutting off the last element of each one, because the while loop overshoots tend by one timepoint
    G1 = G1[:-1]
    G2 = G2[:-1]
    t = t[:-1]

    if plot_fig:
        f, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=False)
        line1, = ax1.plot(t , G1, color="b")
        line2, = ax2.plot(t , G2, color="r")
        ax1.set_ylabel('G1')
        ax2.set_ylabel('G2')

        ax2.set_xlabel('Time')
        plt.show()




    return([G1,G2,t])









def hill_activation_ssa(get_info=0,tend=1000, params=[1, 0.2, 1, 0.2, 1, 9],init=[0,0],plot_fig=0):
    # params: [k_1, gamma_1, k_2, gamma_2, c, h]

    if get_info:
        print()
        print("TOGGLE SWITCH SSA MODEL")
        print("params: [k_1, gamma_1, k_2, gamma_2, c, h]")
        # print("default: [1, 0.2, 1, 0.2, 1, 9]")
        print(f"default: {params}")

        return()





    G1 = [init[0]]
    G2 = [init[1]]
    t = [0]


    k_1 = params[0]
    gamma_1 = params[1]
    k_2 = params[2]
    gamma_2 = params[3]


    c = params[4]
    h = params[5]


    while t[-1] < tend:

        props = [ k_1, gamma_1 * G1[-1], \
        (G1[-1]**h / (c**h + G1[-1]**h)) * k_2, gamma_2 * G2[-1]]


        prop_sum = sum(props)


        tau = np.random.exponential(scale=1/prop_sum)

        t.append(t[-1] + tau)


        rand = random.uniform(0,1)


        # G1 production event
        if rand * prop_sum <= props[0]:
                G1.append(G1[-1] + 1)
                G2.append(G2[-1])

        # G1 decay event
        elif rand * prop_sum > props[0] and rand * prop_sum <= sum(props[:2]):
                G1.append(G1[-1] - 1)
                G2.append(G2[-1])

        # G2 production event
        elif rand * prop_sum > sum(props[:2]) and rand * prop_sum <= sum(props[:3]):
                G1.append(G1[-1])
                G2.append(G2[-1] + 1)

        # G2 decay event
        elif rand * prop_sum > sum(props[:3]) and rand * prop_sum <= sum(props[:4]):
                G1.append(G1[-1])
                G2.append(G2[-1] - 1)    

    # cutting off the last element of each one, because the while loop overshoots tend by one timepoint
    G1 = G1[:-1]
    G2 = G2[:-1]
    t = t[:-1]

    if plot_fig:
        f, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=False)
        line1, = ax1.plot(t , G1, color="b")
        line2, = ax2.plot(t , G2, color="r")
        ax1.set_ylabel('G1')
        ax2.set_ylabel('G2')

        ax2.set_xlabel('Time')
        plt.show()




    return([G1,G2,t])












def hill_repression_ssa(get_info=0,tend=1000, params=[1, 0.2, 1, 0.2, 1, 9],init=[0,0],plot_fig=0):
    # params: [k_1, gamma_1, k_2, gamma_2, c, h]

    if get_info:
        print()
        print("TOGGLE SWITCH SSA MODEL")
        print("params: [k_1, gamma_1, k_2, gamma_2, c, h]")
        # print("default: [1, 0.2, 1, 0.2, 1, 9]")
        print(f"default: {params}")

        return()





    G1 = [init[0]]
    G2 = [init[1]]
    t = [0]


    k_1 = params[0]
    gamma_1 = params[1]
    k_2 = params[2]
    gamma_2 = params[3]


    c = params[4]
    h = params[5]


    while t[-1] < tend:

        props = [ k_1, gamma_1 * G1[-1], \
        (c**h/ (c**h + G1[-1]**h)) * k_2, gamma_2 * G2[-1]]


        prop_sum = sum(props)


        tau = np.random.exponential(scale=1/prop_sum)

        t.append(t[-1] + tau)


        rand = random.uniform(0,1)


        # G1 production event
        if rand * prop_sum <= props[0]:
                G1.append(G1[-1] + 1)
                G2.append(G2[-1])

        # G1 decay event
        elif rand * prop_sum > props[0] and rand * prop_sum <= sum(props[:2]):
                G1.append(G1[-1] - 1)
                G2.append(G2[-1])

        # G2 production event
        elif rand * prop_sum > sum(props[:2]) and rand * prop_sum <= sum(props[:3]):
                G1.append(G1[-1])
                G2.append(G2[-1] + 1)

        # G2 decay event
        elif rand * prop_sum > sum(props[:3]) and rand * prop_sum <= sum(props[:4]):
                G1.append(G1[-1])
                G2.append(G2[-1] - 1)    

    # cutting off the last element of each one, because the while loop overshoots tend by one timepoint
    G1 = G1[:-1]
    G2 = G2[:-1]
    t = t[:-1]

    if plot_fig:
        f, (ax1, ax2) = plt.subplots(2, sharex=True, sharey=False)
        line1, = ax1.plot(t , G1, color="b")
        line2, = ax2.plot(t , G2, color="r")
        ax1.set_ylabel('G1')
        ax2.set_ylabel('G2')

        ax2.set_xlabel('Time')
        plt.show()




    return([G1,G2,t])