# import the numpy package
import numpy as np

# user have a chance to select the units of the theta
a = input(' please specify the required units(degrees or radians) : ')

# define the function for convert cartesian to polar coordinates
def polar(x,y):
    if a == 'radians':
       r = np.sqrt(x**2 +y**2)  #convertion formula for r
       theta = np.arctan(y/x)  # convertion formula for theta
    else:
       r = np.sqrt(x**2 +y**2)
       theta = np.degrees(np.arctan(y/x))
    return r,theta

matrix = np.random.uniform(-5,5,size=(200,3))      #define the matrix os size 200*3 
new_column =np.sqrt(matrix[ :,1]**2 + matrix[ :, 2]**2)   # creating the new column by sqrtof the sum of squares of second and third columns
new_matrix = np.column_stack((matrix[ :,0] , new_column))   # stacking the first column and new column
x = new_matrix[ :,0]
y = new_matrix[ :, 1]
polar_new = polar(x,y)
print('the polar coorindates of 200*2 matrix is :', polar_new)

