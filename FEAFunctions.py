from numpy.lib.function_base import disp
from Bodies import *
import numpy as np
import math

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

def rad_to_deg(radians):
    return (radians * (180/math.pi))

def print_radial_displacements(displacements,global_displacement=None):
    i = 0
    for displacement in displacements:
        print("Δθ_" + str(i+1) + ": " + str(round((10**3)*displacements[i],5)) + "degrees")
        i += 1
    if global_displacement is not None:
        print("Δθ_global: " + str(round((10**3)*global_displacement,5)) + "degrees")

# TODO add a function to convert displacements to strain (will require workpiece length to calculate)
# TODO add a function to convert strain to stress (will require Young's Modulus to calculate)
    
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
        displacement_col = np.linalg.lstsq(stiffness,force_col,rcond=None)[0] 
        total_displacement = abs(displacement_col[0])+abs(displacement_col[1])
        displacement_col = np.array([0,total_displacement]).T # left side (ΔL_1) is pinned

    # TODO add another if chunk to run the calculations based on stress

    if force == None and displacement == None:
        print("No force/displacement given")
        return

    print_forces(force_col)
    print_displacements(displacement_col)
    # TODO add a function to print stress/strain
    return [force_col,displacement_col]

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
    # TODO add a function to print stress/strain
    return [forces.T[0],displacements.T[0]]
    
# Solves for cantilever deflection (fixed at one end, free at the other)
# Displacement is perpendicular rather than parallel (as in tension)
# All forces/displacements are on the free end
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
    # TODO add a function to print stress/strain
    return [force_col,displacement_col]

def Solve_SimpleAxialTorsion(workpiece,torque=None,rad_displacement=None):
    #coeff = (3 * workpiece.modulus * workpiece.I_xx) / (workpiece.length**3) # P = (3EI / L^3)(delta)
    # TODO calculate the correct coefficient for axial displacement due to torque
    #      this might require adding another enum in Bodies for shear modulus
    #      it would also probably require calculating J (second polar moment of inertia)
    stiffness = (np.eye(2) * 2) - 1.0
    stiffness *= coeff

    if rad_displacement != None and torque == None: # displacement is given, solve for torque
        rad_displacement_col = np.array([0,rad_displacement]).T # left side (Δθ_1) is pinned
        force_col = np.matmul(stiffness,rad_displacement_col) # B = Ax

    if torque != None and rad_displacement == None: # torque is given, solve for displacement
        force_col = np.array([-torque,torque]).T # equal and opposite reaction torque
        # stiffness is a singular matrix, so the method of least squares is needed to solve
        rad_displacement_col = np.linalg.lstsq(stiffness,force_col,rcond=None)[0] 
        total_displacement = abs(rad_displacement_col[0])+abs(rad_displacement_col[1])
        rad_displacement_col = np.array([0,total_displacement]).T # left side (Δθ_1) is pinned

    if torque == None and rad_displacement == None:
        print("No force/displacement given")
        return

    if torque != None and rad_displacement != None:
        print("error in this function")
        return

    rad_displacement_col = rad_to_deg(rad_displacement_col)
    print_forces(force_col)
    print_radial_displacements(rad_displacement_col)

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