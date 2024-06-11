# importing the packages
import numpy as np
import matplotlib.pyplot as plt

#reading th file 
data = 'StrengthDataForPltting(1).dat'
#process each line
days = []
strength = []

with open(data,'r') as file:
     lines = file.readlines()

for line in lines[1:]:
    values = line.split()
    if len(values)>1:
      days.append(float(values[0]))
      strength.append(list(map(float,values[1:])))

#finding the longest row
max_length = max(len(row) for row in strength)


strength_padded = [row + [np.nan] * (max_length -len(row)) for row in strength]

days = np.array(days)
strength = np.array(strength_padded)

# performing the mean and deviation
mean = np.nanmean(strength, axis=1)
deviation = np.nanstd(strength,axis=1)


# plotting bar
plt.figure()
plt.bar(days,mean,yerr = deviation)
plt.xlabel('days')
plt.ylabel('strength')
plt.title('materials strength')
plt.legend()
plt.grid(True)
plt.show()

#plotting for scatter plot
colors = ['b','g','r','c','m']
plt.figure()
for i,(d,ms) in enumerate(zip(days,mean)):
     plt.scatter([d]*len(strength[i]),strength[i],s=ms*0.1,color = colors[i],label=f'day{d}')
plt.xlabel('day')
plt.ylabel('strength')
plt.title('material strength scatter plot')
plt.legend()
plt.grid(True)
plt.show()

