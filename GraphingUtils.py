import numpy as np
import matplotlib.pyplot as plt

def graph_forces(data):
    xx = np.arange(len(data))
    plt.xlabel('Node')
    plt.ylabel('Force (N)')
    plt.title('Force')
    plt.plot(xx, data)
    plt.show()
    
def graph_displacements(data):
    for i in reversed(range(len(data))):
        data[i] += sum(data[:i])
    data *= 10**3 # convert m to mm
    xx = np.arange(len(data))
    plt.xlabel('Node')
    plt.ylabel('Displacement (mm)')
    plt.title('Global Displacement')
    plt.plot(xx, data)
    plt.show()

def graph_strains(data):
    xx = np.arange(len(data))
    plt.xlabel('Node')
    plt.ylabel('Strain')
    plt.title('Strain')
    plt.plot(xx, data)
    plt.show()

def graph_stress(data):
    xx = np.arange(len(data))
    data *= 10**6 # Pa to MPa
    plt.xlabel('Node')
    plt.ylabel('Stress (MPa)')
    plt.title('Stress')
    plt.plot(xx, data)
    plt.show()

def plot_func_data(func_data):
    choice = -1
    while choice != 0:
        print('') # line break
        print('0) Exit')
        print('1) Force')
        print('2) Displacement')
        print('3) Strain')
        print('4) Stress')
        choice = int(input('Select a graph to plot or 0 to exit.'))
        if choice == 1: # force
            graph_forces(func_data[0])
        if choice == 2: # displacement
            graph_displacements(func_data[1])
        if choice == 3: # strain
            graph_strains(func_data[2])
        if choice == 4: # stress
            graph_stress(func_data[3])

def graph_timing(n_list,time_list):
    plt.xlabel('Nodes')
    plt.ylabel('Runtime (ms)')
    plt.title('Axial Tension Runtime vs. Node Count')
    plt.figure().set_yscale('log')
    plt.plot(n_list, time_list)
    plt.show()