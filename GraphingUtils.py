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
    
def graph_displacements(disp):
    for i in reversed(range(len(disp))):
        disp[i] += sum(disp[:i])
    xx = np.arange(len(disp))
    plt.xlabel('x (m)')
    plt.ylabel('Displacement (m)')
    plt.title('Global Displacement')
    plt.plot(xx, disp)
    plt.show()

