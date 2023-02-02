from Vector import Vector

def point_L1L2(r, m1, m2, sign):
    x = r * (m2/m1/3)**(1/3)
    
    return Vector(r-x, 0) if sign < 0 else Vector(r+x, 0)

