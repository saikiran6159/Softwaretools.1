import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('tensileDeformation.dat',names=True)

part1 = data[:4000]
part2 = data[4001:]

#plotting
fig,ax=plt.subplots(2,2,figsize=(12,8))
ax[0,0].plot(part1['Step'],part1['PotEng'],label='PotEng')
ax[0,0].set_xlabel('Time')
ax[0,0].set_ylabel('PotEng')
ax[0,1].plot(part1['Step'],part1['KinEng'],label='KinEng')
ax[0,1].set_xlabel('Time')
ax[0,1].set_ylabel('KinEng')
ax[1,0].plot(part1['Step'],part1['Temp'],label='Temp')
ax[1,0].set_xlabel('Time')
ax[1,0].set_ylabel('Temp')
ax[1,1].plot(part1['Step'],part1['Press'],label='Press')
ax[1,1].set_xlabel('Time')
ax[1,1].set_ylabel('Press')
plt.legend()
plt.grid(True)
plt.show()

#cal of eps

eps = (part2['Lx']-part2['Lx'][0]/part2['Lx'][0])
#plotting 
plt.figure(figsize=(15,12))
fig,ax=plt.subplots(3,2) 
ax[0,0].plot(part2['Step'],part2['PotEng'],label='PotEng')
ax[0,0].set_xlabel('Time')
ax[0,0].set_ylabel('PotEng')
ax[0,1].plot(part2['Step'],part2['KinEng'],label='KinEng')
ax[0,1].set_xlabel('Time')
ax[0,1].set_ylabel('KinEng')
ax[1,0].plot(part2['Step'],part2['Temp'],label='Temp')
ax[1,0].set_xlabel('Time')
ax[1,0].set_ylabel('Temp')
ax[1,1].plot(eps,part2['Pxx'],label='Pxx')
ax[1,1].set_xlabel('eps')
ax[1,1].set_ylabel('Pxx')
ax[2,0].plot(part2['Step'],part2['Pyy'],label='Pyy')
ax[2,0].plot(part2['Step'],part2['Pzz'],label='Pzz')
ax[2,0].set_xlabel('Time')
ax[2,0].set_ylabel('Pyy and Pzz')
ax[2,1].plot(part2['Step'],part2['Pxy'],label='Pxy')
ax[2,1].plot(part2['Step'],part2['Pxz'],label='Pxz')
ax[2,1].plot(part2['Step'],part2['Pyz'],label='Pyz')
ax[2,1].set_xlabel('Time')
ax[2,1].set_ylabel('Pxy,Pxz and Pyz')
plt.legend()
plt.grid(True)
plt.show()
