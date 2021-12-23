import Bodies
import FEAFunctions as FEA
import GraphingUtils as gu
import time

# Runs FEA.Solve_MultipleAxialTension at each of the node counts given
def test_MultipleAxialTension(n_list):
    testpiece = Bodies.Rod(Bodies.Elasticity.ALUMINUM.value,.05,10) # 10m long Aluminum rod with radius .05m
    time_list = []
    for n in n_list:
        print('Node count: ' + str(n))
        force = [(n,50000)] # 50,000N force on end node
        start = time.time_ns()
        FEA.Solve_MultipleAxialTension(testpiece,force,n,verbose=False)
        end = time.time_ns()
        time_list.append((end-start) / (10**6)) # record time elapsed in ms
    return time_list

def main():
    #node_count_list = [8,16,32,64,128,256,512,1028,2048]
    node_count_list = list(range(100,5000,100))
    xx = node_count_list
    time_list = test_MultipleAxialTension(node_count_list)
    print('Node Count')
    print(node_count_list)
    print(time_list)
    print('Timing (ms)')
    gu.graph_timing(xx,time_list)

main()