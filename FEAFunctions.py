from Bodies import *
import numpy as np

# All equations are copied/derived from
# https://enterfea.com/finite-element-analysis-by-hand/

def print_forces(forces):
    i = 0
    for force in forces:
        print("F_" + str(i+1) + ": " + str(round(forces[i],5)) + "N")
        i += 1

def print_displacements(displacements):
    i = 0
    for displacement in displacements:
        print("ΔL_" + str(i+1) + ": " + str(round((10**3)*displacements[i],5)) + "mm")
        i += 1

# This is from the first simple example
# Solves setup given EITHER force (N) or displacement (m)
# Force and displacement are both numpy column vectors
def Solve_SimpleAxialTension(workpiece,force=None,displacement=None):
    coeff = (workpiece.area * workpiece.modulus) / workpiece.length # AE / L
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



# Function tests
# Results can be verified with
# https://www.omnicalculator.com/physics/stress
piece = SquarePrism(Elasticity.ALUMINUM.value,.1,5)
#Solve_SimpleAxialTension(piece)
#Solve_SimpleAxialTension(piece,displacement=.01)
Solve_SimpleAxialTension(piece,force=400000)