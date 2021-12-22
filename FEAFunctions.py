from numpy.lib.function_base import disp
from Bodies import *
import numpy as np

# All equations are copied/derived from
# https://enterfea.com/finite-element-analysis-by-hand/

def print_forces(forces):
    i = 0
    for force in forces:
        print("F_" + str(i+1) + ": " + str(round(forces[i],5)) + "N")
        i += 1

def print_displacements(displacements,global_displacement=None):
    i = 0
    for displacement in displacements:
        print("ΔL_" + str(i+1) + ": " + str(round((10**3)*displacements[i],5)) + "mm")
        i += 1
    if global_displacement is not None:
        print("ΔL_global: " + str(round((10**3)*global_displacement,5)) + "mm")
        
    
# This is from the first simple example
# Solves setup given EITHER force (N) or displacement (m)
# Force and displacement are both numpy column vectors
def Solve_SimpleAxialTension(workpiece,force=None,displacement=None):
    coeff = (workpiece.area * workpiece.modulus) / workpiece.length # P = (AE / L)(delta)
    stiffness = (np.eye(2) * 2) - 1.0
    stiffness *= coeff

    if displacement != None and force == None: # displacement is given, solve for force
        displacement_col = np.array([0,displacement]).T # left side (ΔL_1) is pinned
        force_col = np.matmul(stiffness,displacement_col) # B = Ax

    if force != None and displacement == None: # force is given, solve for displacement
        force_col = np.array([-force,force]).T # equal and opposite reaction force
        # stiffness is a singular matrix, so the method of least squares is needed to solve
        displacement_col = np.linalg.lstsq(stiffness,force_col)[0] 
        total_displacement = abs(displacement_col[0])+abs(displacement_col[1])
        displacement_col = np.array([0,total_displacement]).T # left side (ΔL_1) is pinned

    if force == None and displacement == None:
        print("No force/displacement given")
        return

    print_forces(force_col)
    print_displacements(displacement_col)

# Allows you to solve for local/global displacement, given pairs of locations and forces.
# The area is assumed to be the same along the entire piece.
# force_pos_pairs is an array of (node,force) tuples. Positive force = tension.
def Solve_MultipleAxialTension(workpiece,pos_force_pairs,nodes):
    node_length = workpiece.length / (nodes*(.5*(nodes-1))) # why does this line work? couldn't tell you.
    coeff = (workpiece.area * workpiece.modulus) / node_length
    local_stiffness = (np.eye(2) * 2) - 1.0
    local_stiffness *= coeff
    global_stiffness = np.zeros([nodes,nodes])
    for i in range(nodes-1):
        global_stiffness[i:i+2,i:i+2] += local_stiffness
    forces = np.zeros([nodes,1])
    for pair in pos_force_pairs:
        pos, force = pair
        forces[pos-1] += force
    forces[0] = -sum(forces)
    displacements = np.linalg.lstsq(global_stiffness,forces,rcond=None)[0]
    offset = 0
    for i in range(nodes-1):
        if displacements[i] < 0:
            offset -= displacements[i]
    #displacements += offset
    offset = -displacements[0]
    #displacements -= displacements[0]
    #print(displacements)
    #print_displacements(displacements.T[0],global_displacement=sum(displacements.T[0]))
    for i in range(len(displacements)):
        #print(i)
        #if displacements[i] < 0 or sum(forces[i:]) != 0:
            #print(str(i) + " is not zero")
        displacements[i] += offset
        #else:
            #displacements[i] = 0
        #if sum(forces[i:]) == 0:
            #displacements[i] = 0
    print_forces(forces.T[0])
    print_displacements(displacements.T[0],global_displacement=sum(displacements.T[0]))
    
def Solve_SimpleCantileverDeflection(workpiece,force=None,displacement=None):
    coeff = (3 * workpiece.modulus * workpiece.I_xx) / (workpiece.length**3) # P = (3EI / L^3)(delta)
    stiffness = (np.eye(2) * 2) - 1.0
    stiffness *= coeff

    if displacement != None and force == None: # displacement is given, solve for force
        displacement_col = np.array([0,displacement]).T # left side (ΔL_1) is pinned
        force_col = np.matmul(stiffness,displacement_col) # B = Ax

    if force != None and displacement == None: # force is given, solve for displacement
        force_col = np.array([-force,force]).T # equal and opposite reaction force
        # stiffness is a singular matrix, so the method of least squares is needed to solve
        displacement_col = np.linalg.lstsq(stiffness,force_col,rcond=None)[0] 
        total_displacement = abs(displacement_col[0])+abs(displacement_col[1])
        displacement_col = np.array([0,total_displacement]).T # left side (ΔL_1) is pinned

    if force == None and displacement == None:
        print("No force/displacement given")
        return

    if force != None and displacement != None:
        print("error in this function")
        return

    print_forces(force_col)
    print_displacements(displacement_col)

#reads txt file with input values and puts them into solver functions
def read_input():
    print("\n<< Finite Element Analysis Calculator >>\nby Colton Kreischer and Griffin Robjohns\n")
    readfile = input("Name of Input File: ")
    with open(readfile) as file:
        data = file.readlines()
    file.close()
    inputs = []
    for line in data:
        index = line.find("=")
        line = line[index+1:-1]
        inputs.append(line)
    part = inputs[0]
    length_i = inputs[1]
    diameter_i = inputs[2]
    width_i = inputs[3]
    base_i = inputs[4]
    height_i = inputs[5]
    solver = inputs[6]
    material_i = inputs[7]
    force_i = inputs[8]
    displacement_i = inputs[9]
    len(force_i)
    len(displacement_i)
    if len(force_i) > 1:
        force_i = float(force_i)
    else:
        force_i = None
    if len(displacement_i) > 1:
        displacement_i = float(displacement_i)
    else:
        displacement_i = None
        
    print("Thank You!\nCalculating...\n")
    matstr = getattr(Elasticity, material_i)
    if part == "RD":
        piece = Rod(matstr.value,radius=(float(diameter_i)/2.0),length=float(length_i))
    elif part == "SP":
        piece = SquarePrism(matstr.value,width=float(width_i),length=float(length_i))
    elif part == "RP":
        piece = RectangularPrism(matstr.value,base=float(base_i),height=float(height_i),length=float(length_i))
    if solver == "SAT":
        Solve_SimpleAxialTension(piece,force=force_i,displacement=displacement_i)
    elif solver == "SAT":
        print("In Progress..")
        # Solve_MultipleAxialTension(piece,force=input6,displacement=input7)
    elif solver == "SCD":
        Solve_SimpleCantileverDeflection(piece,force=force_i,displacement=displacement_i)

read_input()
## Function tests
#  Results can be verified with
#  https://www.omnicalculator.com/physics/stress
#  https://www.omnicalculator.com/construction/beam-deflection 

# piece = SquarePrism(Elasticity.ALUMINUM.value,width=0.1,length=5)

#Solve_SimpleAxialTension(piece)
#Solve_SimpleAxialTension(piece,displacement=.01)

#Solve_SimpleAxialTension(piece,force=50000)
#Solve_MultipleAxialTension(piece,[(5,50000)],10)
#Solve_MultipleAxialTension(piece,[(5,50000)],5)

funcs = [Solve_SimpleAxialTension,
         Solve_MultipleAxialTension,
         Solve_SimpleCantileverDeflection]

# Solve_SimpleCantileverDeflection(piece,displacement=.1)