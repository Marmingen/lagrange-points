#############################################################
## IMPORT

from math import sqrt

#############################################################
## VECTOR

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"[{self.x}, {self.y}]"
    
    def __repr__(self):
        return self.__str__()
        
    def scalar_m(self, sca):
        return Vector(sca*self.x, sca*self.y)
    
    def norm(self):
        ab = abs(self)
        return Vector(self.x/ab, self.y/ab)
    
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)
    
    def __mul__(self, other):
        return self.x*other.x+self.y*other.y