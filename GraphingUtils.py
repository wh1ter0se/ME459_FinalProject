import numpy as np
import matplotlib.pyplot as plt

def graph_data(data):
    xx = np.arange(len(data))
    plt.plot(xx, data)
    plt.show()

def graph_forces(data):
    xx = np.arange(len(data))
    plt.xlabel('x (m)')
    plt.ylabel('Force (N)')
    plt.plot(xx, data)
    plt.show()
    
def graph_displacements(data):
    for i in reversed(range(len(data))):
        data[i] += sum(data[:i])
    xx = np.arange(len(data))
    plt.xlabel('x (m)')
    plt.ylabel('Displacement (m)')
    plt.title('Global Displacement')
    plt.plot(xx, data)
    plt.show()

def graph_strains(data):
    xx = np.arange(len(data))
    plt.xlabel('x (m)')
    plt.ylabel('Strain')
    plt.plot(xx, data)
    plt.show()

def graph_stress(data):
    xx = np.arange(len(data))
    data *= 10**6 # Pa to MPa
    plt.xlabel('x (m)')
    plt.ylabel('Stress (MPa)')
    plt.plot(xx, data)
    plt.show()

def plot_func_data(func_data):
    choice = -1
    while choice != 0:
        print('') # line break
        print('0) Exit')
        print('1) Force')
        print('2) Displacement')
        print('3) Strain') # TODO implement
        print('4) Stress') # TODO implement
        choice = int(input('Select a graph to plot or 0 to exit:'))
        if choice == 1: # force
            graph_forces(func_data[0])
        if choice == 2: # displacement
            graph_displacements(func_data[1])
        if choice == 3: # strain
            graph_strains(func_data[2])
        if choice == 4: # stress
            graph_stress(func_data[3])