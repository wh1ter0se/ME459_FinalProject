from Bodies import *

def generator():
    print("\n<< Finite Element Analysis Calculator Input Generator >>\n")
    print("Input workpiece type \nRD = Rod\nSP = Square Prism\nRP = Rectangular Prism")
    while True:
        input1 = input(":")
        if input1 == "RD" or input1 == "SP" or input1 == "RP":
            break
        else:
            print("Not valid input. Try again.")
    print("Input length (m) [cannot exceed 1000 meters]")
    while True:
        input2 = input(":")
        if float(input2) <= 1000.0 and float(input2) > 0.0:
            break
        else:
            print("Not valid input. Try again.")
    if input1 == "RD":
        input3str = "diameter"
    elif input1 == "SP":
        input3str = "width"
    else:
        input3str = "base"
    print("Input " + input3str + " (m) [cannot exceed 1000 meters]")
    while True:
        input3 = input(":")
        if float(input3) <= 1000.0 and float(input3) > 0.0:
            break
        else:
            print("Not valid input. Try again.")
    if input1 == "RP":
        print("Input height (m) [cannot exceed 1000 meters]")
        while True:
            input4 = input(":")
            if float(input4) <= 1000.0 and float(input4) > 0.0:
                break
            else:
                print("Not valid input. Try again.")
    print("Input calculator type \nSAT = Simple Axial Tension")
    print("MAT = Multiple Axial Tension\nSCD = Simple Cantilever Deflection")
    while True:
        input5 = input(":")
        if input5 == "SAT" or input5 == "MAT" or input5 == "SCD":
            break
        else:
            print("Not valid input. Try again.")
    print("Input forces (N) [cannot exceed 100kN]")
    while True:
        input6 = input(":")
        if float(input6) <= 100000.0 and float(input6) >= 0.0:
            break
        else:
            print("Not valid input. Try again.")
    if float(input6) == 0.0:
        input6 = " "
    print("Input displacement (m) [cannot exceed 10 meters]")
    while True:
        input7 = input(":")
        if float(input7) <= 10000.0 and float(input7) >= 0.0:
            break
        else:
            print("Not valid input. Try again.")
    if float(input7) == 0.0:
        input7 = " "
    print("Input material")
    while True:
        input8 = input(":")
        try:
            testvar = getattr(Elasticity, input8)
            break
        except AttributeError:
            print("Not valid input. Try again.")
    lines = []
    if input1 == "RD":  
        lines = ['type=' + input1, 'length=' + input2, 'diameter=' + input3, 'width=', 'base=', 'height=',
        'solver=' + input5, 'material=' + input8, 'forces=' + input6, 'displacement=' + input7]
    elif input1 == "SP":
        lines = ['type=' + input1, 'length=' + input2, 'diameter=', 'width=' + input3, 'base=', 'height=',
        'solver=' + input5, 'material=' + input8, 'forces=' + input6, 'displacement=' + input7]
    else:
        lines = ['type=' + input1, 'length=' + input2, 'diameter=', 'width=', 'base=' + input3, 'height=' + input4,
        'solver=' + input5, 'material=' + input8, 'forces=' + input6, 'displacement=' + input7]
    with open('FEA_Inputs_' + input1 + '_' + input5 + '.txt', 'w') as file:
        for line in lines:
            file.write(line)
            file.write('\n')
    file.close()
    print("Generation Successful!")
generator()