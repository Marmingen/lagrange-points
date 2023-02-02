#############################################################
## IMPORTS

from Vector import Vector

#############################################################
## POINT

class Point():
    
    def __init__(self, canvas, pos = (400,250), mass = 1e8, radius = 4, color="#CF333A", tag="Point"):
        self.canvas = canvas
        self.pos = Vector(pos[0], pos[1])
        self.mass = mass
        self.radius = radius
        self.color = color
        self.tag = tag
        self.create_body()
                
    def create_body(self):
        self.item = self.canvas.create_oval(self.pos.x - self.radius, self.pos.y-self.radius, self.pos.x+self.radius, self.pos.y + self.radius, fill = self.color, outline = "black", tags=self.tag)

    def set_radius(self, new_radius):
        self.radius = new_radius
        self.create_body()
        
    def move(self,x ,y):
        self.pos = Vector(x + self.radius, y + self.radius)
        self.canvas.moveto(self.item, int(x)-self.radius-1, int(y)-self.radius-1)