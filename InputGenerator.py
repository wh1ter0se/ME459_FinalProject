from Bodies import *

# generator is completely robust and does not fail even when illogical values are inputted
# used to generate scenario for multiple calculation in solvers
# can make smaller adjustments in txt file faster than creating new scenario for each run

def generator():
    print("\n<< Finite Element Analysis Calculator Input Generator >>\n")

    # ask for piece type
    print("Input workpiece type \nRD = Rod\nSP = Square Prism\nRP = Rectangular Prism")
    while True:
        input1 = input(":")
        input1 = input1.upper()
        if input1 == "RD" or input1 == "SP" or input1 == "RP":
            break
        else:
            print("Not valid input. Try again.")
    
    # ask for piece length
    print("Input length (m) [cannot exceed 1000 meters]")
    while True:
        try:
            input2 = input(":")
            if float(input2) <= 1000.0 and float(input2) > 0.0:
                break
            else:
                print("Not valid input. Try again.")
        except ValueError:
            print("Not valid input. Try again.")
    
    # ask for diameter/width/depending on piece type
    if input1 == "RD":
        input3str = "diameter"
    elif input1 == "SP":
        input3str = "width"
    else:
        input3str = "base"
    print("Input " + input3str + " (m) [cannot exceed 1000 meters]")
    while True:
        try:
            input3 = input(":")
            if float(input3) <= 1000.0 and float(input3) > 0.0:
                break
            else:
                print("Not valid input. Try again.")
        except ValueError:
            print("Not valid input. Try again.")

    # ask for height if needed
    if input1 == "RP":
        print("Input height (m) [cannot exceed 1000 meters]")
        while True:
            try:
                input4 = input(":")
                if float(input4) <= 1000.0 and float(input4) > 0.0:
                    break
                else:
                    print("Not valid input. Try again.")
            except ValueError:
                print("Not valid input. Try again.")
    
    # ask for solver type
    print("Input calculator type \nSAT = Simple Axial Tension")
    print("MAT = Multiple Axial Tension\nSCD = Simple Cantilever Deflection")
    while True:
        input5 = input(":")
        input5 = input5.upper()
        if input5 == "SAT" or input5 == "MAT" or input5 == "SCD":
            break
        else:
            print("Not valid input. Try again.")

    # ask for force or displacement
    if input5 != "MAT":
        print("Input input type \nF = Force\nD = Displacement")
        while True:
            input5a = input(":")
            input5a = input5a.upper()
            if input5a == "F" or input5a == "D":
                break
            else:
                print("Not valid input. Try again.")
    elif input5 == "MAT":
        input5a = "M"
        print("Input number of nodes [maximum of 8]")
        while True:
            try:
                input5b = input(":")
                if int(input5b) <= 8 and int(input5b) > 0:
                    break
                else:
                    print("Not valid input. Try again.")
            except ValueError:
                print("Not valid input. Try again.")
        i = 0
        mult_forces = []
        for i in range(int(input5b)):
            print("Input force (N) for node " + str(i+1) + " [cannot exceed 100kN]")
            while True:
                try:
                    input6a = input(":")
                    if float(input6a) <= 100000.0 and float(input6a) > 0.0:
                        break
                    else:
                        print("Not valid input. Try again.")
                except ValueError:
                    print("Not valid input. Try again.")
            mult_forces.append(input6a)

    # ask for force or displacement values
    # if "F" entered then ask for force, if "D" entered then ask for displacement
    input6 = None
    input7 = None
    input6a = None
    if input5a == "F":
        print("Input forces (N) [cannot exceed 100kN]")
        while True:
            try:
                input6 = input(":")
                if float(input6) <= 100000.0 and float(input6) >= 0.0:
                    break
                else:
                    print("Not valid input. Try again.")
            except ValueError:
                print("Not valid input. Try again.")
        if float(input6) == 0.0:
            input6 = " "
    elif input5a == "D":
        print("Input displacement (m) [cannot exceed 10 meters]")
        while True:
            try:
                input7 = input(":")
                if float(input7) <= 10000.0 and float(input7) >= 0.0:
                    break
                else:
                    print("Not valid input. Try again.")
            except ValueError:
                print("Not valid input. Try again.")
        if float(input7) == 0.0:
            input7 = " "
    if input6 == None:
        input6 = ""
    if input7 == None:
        input7 = ""
    if input5 == "MAT":
        input6 = mult_forces

    #ask for material
    print("Input material")
    while True:
        input8 = input(":")
        input8 = input8.upper()
        try:
            getattr(Elasticity, input8)
            break
        except AttributeError:
            print("Not valid input. Try again.")
    
    # set array based on input variables
    lines = []
    if input1 == "RD":  
        lines = ['type=' + input1, 'length=' + input2, 'diameter=' + input3, 'width=', 'base=', 'height=',
        'solver=' + input5, 'material=' + input8, 'forces=' + str(",".join(input6)), 'displacement=' + input7]
    elif input1 == "SP":
        lines = ['type=' + input1, 'length=' + input2, 'diameter=', 'width=' + input3, 'base=', 'height=',
        'solver=' + input5, 'material=' + input8, 'forces=' + str(",".join(input6)), 'displacement=' + input7]
    elif input1 == "RP":
        lines = ['type=' + input1, 'length=' + input2, 'diameter=', 'width=', 'base=' + input3, 'height=' + input4,
        'solver=' + input5, 'material=' + input8, 'forces=' + str(",".join(input6)), 'displacement=' + input7]
    
    # write txt file with input array
    with open('FEA_Inputs_' + input1 + '_' + input5 + '.txt', 'w') as file:
        for line in lines:
            file.write(line)
            file.write('\n')
    file.close()

    print("Generation Successful!")
    print('Filename: FEA_Inputs_' + input1 + '_' + input5 + '.txt')

generator()