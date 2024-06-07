from math import *
def cart(x,y):
    r=sqrt(x**2+y**2)
    theta=atan(y/x)
    return r,theta
def polar(r,theta):
    x=r*cos(theta)
    y=r*sin(theta)
    return x,y

