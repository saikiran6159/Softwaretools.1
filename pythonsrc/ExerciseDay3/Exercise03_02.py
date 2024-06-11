# importing the packages
import numpy as np
import matplotlib.pyplot as plt

#defining the axes region
x = np.linspace(-2*np.pi,2*np.pi,1000)
y = np.linspace(-2,3,1000)

#plotting
plt.figure()
plt.subplot(131)
plt.plot(np.sin(x),y,color='red')  # plotting for sin function
plt.xlabel('sin(x)')
plt.ylabel('y-axis')
plt.title('sin finction')

plt.subplot(132)
plt.plot(np.cos(x),y,linestyle='--',color='blue')  #plotting for cos function
plt.xlabel('cos(x)')
plt.ylabel('y-axis')
plt.title('cos finction')

plt.subplot(133)
plt.plot(np.cos(x+(np.pi/4)),y,linestyle=':',color='green')   # plotting for cosin function
plt.xlabel('cos(x+pi/4)')
plt.ylabel('y-axis')
plt.title('cos finction')

plt.legend()
plt.grid(True)
plt.show()
