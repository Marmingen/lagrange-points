#############################################################
## IMPORTS

from math import sin, cos, acos
from Vector import Vector

#############################################################
## FUNCTIONS

def calc_theta(input):
    return acos(input.x/abs(input))

def rotation(input, theta):
    x = input.x*cos(theta)-input.y*sin(theta)
    y = input.x*sin(theta)+input.y*cos(theta)
    return Vector(int(x+0.5),int(y+0.5))

#############################################################
## RUNCODE

if __name__ == "__main__":
    pass