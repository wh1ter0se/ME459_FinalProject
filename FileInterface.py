import FEAFunctions as FEA
import Bodies

# Reads txt file with input values and puts them into solver functions
# used to save certain/specific inputs scenarios, better for bigger/long-time input calculations
# as opposed to live interface, which is dynamic
def read_input():
    print("\n<< Finite Element Analysis Calculator >>\nby Colton Kreischer and Griffin Robjohns\n")
    readfile = input("Name of Input File: ") #ask for file name
    with open(readfile) as file: #open named file
        data = file.readlines()
    file.close()
    inputs = []
    node_forces = []
    # takes each line of txt file and returns inputs as variables
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
    # if solver == "MAT":
    #     nodes = inputs[8].count(",") + 1 
    #     for nodes in inputs[8]:
    #         ind = inputs[8].find(",")
    #         add = inputs[8][0:ind]
    #         inputs[8].replace(add, "")
    #         node_forces.append(add)
    #     force_i = node_forces
    # else:
    force_i = inputs[8]
    # print(force_i)
    material_i = inputs[7]
    displacement_i = inputs[9]
    # if solver == "MAT":
    #     x = 0
    #     for x in force_i:
    #         force_i[x] = float(force_i[x])
    # else:
    if len(force_i) > 1:
        force_i = float(force_i)
    else:
        force_i = None
    if len(displacement_i) > 1:
        displacement_i = float(displacement_i)
    else:
        displacement_i = None
    
    # execute solvers based on inputs
    print("Thank You!\nCalculating...\n")
    matstr = getattr(Bodies.Elasticity, material_i)
    if part == "RD":
        piece = Bodies.Rod(matstr.value,radius=(float(diameter_i)/2.0),length=float(length_i))
    elif part == "SP":
        piece = Bodies.SquarePrism(matstr.value,width=float(width_i),length=float(length_i))
    elif part == "RP":
        piece = Bodies.RectangularPrism(matstr.value,base=float(base_i),height=float(height_i),length=float(length_i))
    if solver == "SAT":
        FEA.Solve_SimpleAxialTension(piece,force=force_i,displacement=displacement_i)
    elif solver == "MAT":
        print("In Progress...")
        # FEA.Solve_MultipleAxialTension(piece,force=force_i,displacement=displacement_i)
    elif solver == "SCD":
        FEA.Solve_SimpleCantileverDeflection(piece,force=force_i,displacement=displacement_i)

read_input()