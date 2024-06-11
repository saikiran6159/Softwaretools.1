# importing the packages
import numpy as np
import matplotlib.pyplot as plt

#defining the region of x,y
x = np.linspace(-2,2,100)
y = np.linspace(-1,3,100)

# define the function f

f = (((1-x)**2) + 100 *(y-x**2)**2)


#plotting 
plt.figure()
plt.plot(x,y,f,color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

print('the minimun of the function: ' ,min(f)) # directly find the min value of f


