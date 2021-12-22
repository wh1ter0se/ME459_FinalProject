import FEAFunctions as FEA
import Bodies
import GraphingUtils as gu

# Either retrieves a modulus of elasticity from the list of known materials
# or gets a custom value from user input
def get_modulus():
    i = 0
    materials = []
    print('') # line break
    for material in Bodies.Elasticity: # print out all available materials
        materials.append(material)
        print(str(i+1) + ') ' + material.name)
        i += 1
    print(str(i+1)+') Custom material (enter Young\'s modulus manually)')
    choice = int(input('Select material ID: ')) - 1 # have user select material
    if choice == i:
        modulus = input('Enter Young\'s Modulus of material in Pa: ')
    else:
        modulus = materials[choice].value
    return modulus

# Generates and returns a workpiece using user input
def get_workpiece():
    i = 0
    print('') # line break
    for ptype in Bodies.piecetypes: # print out all available workpiece types
        print(str(i+1) + ') ' + ptype.__name__)
        i += 1
    choice = int(input('Select workpiece type ID: ')) - 1 # have user select workpiece type
    piecetype = Bodies.piecetypes[choice]
    # init_func = piecetype.__init__
    # func_args = init_func.__code__.co_varnames[:init_func.__code__.co_argcount] # get function arguments
    # func_args = func_args [1:-1] # remove self and length from list

    modulus = get_modulus()
    length = float(input('Length (m): '))   # TODO find a way to do this without if-statements
    if piecetype == Bodies.Rod:
        radius = float(input('Radius (m): '))
        workpiece = Bodies.Rod(modulus,radius,length)
    if piecetype == Bodies.SquarePrism:
        width = float(input('Width (m): '))
        workpiece = Bodies.SquarePrism(modulus,width,length)
    if piecetype == Bodies.RectangularPrism:
        base = float(input('Base width (m): '))
        height = float(input('Height (m): '))
        workpiece = Bodies.RectangularPrism(modulus,base,height,length)

    return workpiece

# Prints all available FEA functions
# Returns user selection
def get_function():
    i = 0
    print('') # line break
    for func in FEA.funcs: # print out all available functions
        print(str(i+1) + ') ' + func.__name__)
        i += 1
    choice = int(input('Select function ID: ')) - 1 # have user select function
    return FEA.funcs[choice]

def run_FEA_func(func,workpiece):
    func_args = func.__code__.co_varnames[:func.__code__.co_argcount] # get function arguments
    print('') # line break
    if 'pos_force_pairs' in func_args: # multiple-load function
        print('This is a multiple-load function.')
        nodes = int(input('Enter number of nodes (discrete sections): '))
        choice = -1
        pos_force_pairs = []
        while (choice != 0):
            choice = float(input('Enter a force (N) or 0 to finish entering force-position pairs: '))
            if choice != 0:
                force = choice
                pos = int(input('Enter node position for force (1-' + str(nodes) + ')'))
                pos_force_pairs.append((pos,force))
        print('') # line break
        func_data = func(workpiece,pos_force_pairs,nodes)
    elif ('force' in func_args) and ('displacement' in func_args): # single-load function, force OR displacement
        print('This function can be driven by either a known force or a known displacement.')
        print('1) Force')
        print('2) Displacement')
        choice = int(input('Select option: '))
        if choice == 1:
            print('Positive force correlates with tension')
            force = float(input('Force (N): '))
            print('') # line break
            func_data = func(workpiece,force=force)
        else:
            print('Positive displacement correlates with tension')
            displacement = float(input('Displacement (m): '))
            print('') # line break
            func_data = func(workpiece,displacement=displacement)
    plot_func_data(func_data)

def plot_func_data(func_data):
    choice = -1
    while choice != 0:
        print('0) Exit')
        print('1) Force')
        print('2) Displacement')
        print('3) Stress') # TODO implement
        print('4) Strain') # TODO implement
        choice = int(input('Select a graph to plot or 0 to exit.'))
        if choice == 1: # force
            gu.graph_forces(func_data[0])
        if choice == 2: # displacement
            gu.graph_displacements(func_data[1])

def main():
    chosen_piece = get_workpiece()
    print('\n-----------------------')
    print(  'Workpiece Summary: ')
    print('Workpiece type: ' + chosen_piece.__class__.__name__)
    chosen_piece.summary()
    print('-----------------------')
    chosen_func = get_function()
    run_FEA_func(chosen_func,chosen_piece)
    
main()

#elif ('displacement' in func_args) and ('')