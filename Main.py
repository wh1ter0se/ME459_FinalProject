import FEAFunctions as FEA

i = 0
for func in FEA.funcs: # print out all available functions
    print(str(i+1) + ') ' + func.__name__)
    i += 1
choice = int(input('Select function ID:')) # have user select function
chosen_func = FEA.funcs[choice-1]
print('\nFunction: ' + chosen_func.__name__)

func_args = chosen_func.__code__.co_varnames[:chosen_func.__code__.co_argcount] # get function arguments
if 'pos_force_pairs' in func_args: # multiple-load function
    print('This is a multiple-load function')
