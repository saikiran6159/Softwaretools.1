#import thr numpy package
import  numpy as np

# define the function for elemnet stiffness matrix
def compute_element_stiffness(E,A,L):
    k = (E*A/L)
    return k*np.array([[1,-1],[-1,1]])

# define the function for global stiffness matrix
def global_stiffness(matrix,element_stiffness):
    k_global = np.zeros((matrix,matrix))   # initial assign the zeros values in k matrix
    for i in range(matrix):
        k_global[i:i+2,i:i+2]+=element_stiffness[1:2,1:2]
    return k_global

matrix = 10000

# parameters
E = 200e9
A = 1e-6
L = 1e-4

element_stiffness = compute_element_stiffness(E,A,L)

global_eff = global_stiffness(matrix,element_stiffness)
print(' the global stiffness matrix :',global_eff)


