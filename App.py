from tkinter import *
from tkinter import ttk
from Star import Star
from Body import Body
from Point import Point
from mathematics import *
from Vector import Vector
from math import sin,cos,pi

class App():
    
    def __init__(self):
        self.root = Tk()
        self.root.title("lagrange points")
        
        self.pause = False

        self.width = 400
        
        ###############################
        # setting up the frames
        
        self.top_frame = ttk.Frame(self.root, width=2*self.width, height=2*self.width)
        self.top_frame.grid(column=0, row=0, sticky=(N, W, E, S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.canvas = Canvas(self.top_frame, width=2*self.width, height=2*self.width)
        self.conf_space(self.canvas)
        
        self.option_frame = ttk.Frame(self.top_frame)
        self.conf_opt(self.option_frame)
        
        self.top_frame.columnconfigure(5, weight=1)
        self.top_frame.rowconfigure(3, weight=1)
        
        ###############################
        # initializing the star and asteroid list
        
        self.reset()
        
        ##############################
        # setting up the info-labels
        
        ###############################
        # setting up buttons
        self.add_r_btn = ttk.Button(self.option_frame, text="reset position", command=self.reset)
        self.add_r_btn.grid(column=3,row=0, columnspan=2)
        
        
        ###############################
        # setting up the slider
        
        self.mass_slider = ttk.Scale(self.option_frame, orient=HORIZONTAL, length=100, from_=0.001, to=0.2, command=self.change_mass_body)
        self.mass_slider.grid(column=3, row=2, columnspan=2)
        self.mass_slider.set(0.1)
        
        self.star_slider = ttk.Scale(self.option_frame, orient=HORIZONTAL, length=100, from_=1, to=5, command=self.change_mass_star)
        self.star_slider.grid(column=3, row=1, columnspan=2)
        self.star_slider.set(1)
        
        ###############################
        # setting up drag n drop
        
        self.canvas.tag_bind("Body", "<B1-Motion>", self._relocate)
        
        ###############################

    def conf_space(self, space_canvas):
        space_canvas['height'] = 2*self.width
        space_canvas['width'] = 2*self.width
        space_canvas['borderwidth'] = 2
        space_canvas['relief'] = 'ridge'
        # space_canvas['background'] = '#29292B'
        space_canvas['background'] = 'white'
        
        space_canvas.grid(column=0, row=0, rowspan = 3, columnspan=3,sticky=NW)
        
    def conf_opt(self, option_frame):
        option_frame['height'] = 2*self.width
        option_frame['width'] = 200
        option_frame['padding'] = 5
        option_frame['borderwidth'] = 2
        option_frame['relief'] = 'ridge'

        option_frame.grid(column=3, row=1, rowspan = 1, columnspan=2,sticky=NE)
        
        option_frame.columnconfigure(2, weight=1)
        option_frame.rowconfigure(6, weight=1)

    def start(self):
        self.root.mainloop()
    
    def set_star(self, star):
        self.star = star
        
    def set_body(self, body):
        self.body = body

    def draw_line(self, body1, body2, dash_in=None):
        line = self.canvas.create_line(body1.pos.x,body1.pos.y,body2.pos.x,body2.pos.y, fill="grey", width=1, dash=dash_in)
        self.canvas.tag_lower(line)

        return line

    def reset(self):
        
        self.canvas.delete("all")
        
        self.set_star(Star(self.canvas, pos=(self.width,self.width)))
        
        self.set_body(Body(self.canvas, pos=(self.width+150, self.width)))
        
        self.main_line = self.draw_line(self.star, self.body, (2,2))
        
        self.l3 = Point(self.canvas,pos=(self.width-150,self.width))
        
        self.l3_line = self.draw_line(self.star, self.l3, (2,2))
        
        self.l1 = Point(self.canvas,pos=(self.width + int(point_L1L2(abs(self.body.pos-self.star.pos), self.star.mass, self.body.mass, -1).x+0.5),self.width))
        
        self.l2 = Point(self.canvas,pos=(self.width + int(point_L1L2(abs(self.body.pos-self.star.pos), self.star.mass, self.body.mass, 1).x+0.5),self.width))
        
        self.l2_line = self.draw_line(self.body, self.l2, (2,2))
        
        self.l4 = Point(self.canvas,pos=(self.width + 150*cos(pi/3),self.width+ 150*sin(pi/3)))
        
        self.canvas.tag_lower(self.l1)
        
        self.canvas.tag_lower(self.l2)
        
        self.l4_line = self.draw_line(self.star, self.l4, (2,2))
        
        self.l5 = Point(self.canvas,pos=(self.width+ 150*cos(pi/3),self.width - 150*sin(pi/3)))
        
        self.l5_line = self.draw_line(self.star, self.l5, (2,2))
        
        self.orbit = self.canvas.create_oval(self.width-150, self.width-150, self.width+150, self.width+150, outline = "grey")
            
        self.canvas.tag_lower(self.orbit)
        
        
    def change_mass_body(self, new_mass):
        self.body.mass = float(new_mass)
        
        r = abs(self.body.pos-self.star.pos)
        
        theta = calc_theta(self.body.pos-self.star.pos)
        
        self.update_l1l2(r, theta)
        
    def change_mass_star(self, new_mass):
        self.star.mass = float(new_mass)
        
        r = abs(self.body.pos-self.star.pos)
        
        theta = calc_theta(self.body.pos-self.star.pos)
        
        self.update_l1l2(r, theta)
        
    def update_l1l2(self, r, theta):
        l1_coords = point_L1L2(r, self.star.mass, self.body.mass, -1)
        
        l2_coords = point_L1L2(r, self.star.mass, self.body.mass, 1)
        
        l1_rotated = rotation(l1_coords, theta)
        
        l2_rotated = rotation(l2_coords, theta)
        
        self.l1.move(self.width+l1_rotated.x, self.width-l1_rotated.y if self.body.pos.y < self.width else self.width+l1_rotated.y)
        self.l2.move(self.width+l2_rotated.x, self.width-l2_rotated.y if self.body.pos.y < self.width else self.width+l2_rotated.y)
        
        self.canvas.coords(self.l2_line, [self.body.pos.x,self.body.pos.y,self.l2.pos.x-self.l2.radius,self.l2.pos.y-self.l2.radius])
        
    def calc_Lpoints(self):
        
        theta = calc_theta(self.body.pos-self.star.pos)
        
        r = abs(self.body.pos-self.star.pos)
        
        l3_rotated = rotation(Vector(r,0), theta)
        
        l4_rotated = rotation(Vector(r,0), theta + pi/3)
        
        l5_rotated = rotation(Vector(r,0), theta - pi/3)
        
        self.l3.move(self.width-l3_rotated.x, self.width-l3_rotated.y if self.body.pos.y > self.width else self.width+l3_rotated.y)
        
        self.l4.move(self.width + l4_rotated.x, self.width-l4_rotated.y if self.body.pos.y < self.width else self.width+l4_rotated.y)
        
        self.l5.move(self.width + l5_rotated.x, self.width-l5_rotated.y if self.body.pos.y < self.width else self.width+l5_rotated.y)
        
        self.update_l1l2(r, theta)
        
    def change_orbit(self):
        
        r = abs(self.body.pos-self.star.pos)
        
        self.canvas.coords(self.orbit, [self.width-int(r+0.5), self.width -int(r+0.5), self.width + int(r+0.5), self.width + int(r+0.5)])
        
        self.canvas.tag_lower(self.orbit)
        
    def _relocate(self, event):
        
        def _fix_line(point, line):
            self.canvas.coords(line, [self.width,self.width,point.pos.x-point.radius,point.pos.y-point.radius])
        
        x0,y0 = self.canvas.winfo_pointerxy()
        x0 -= self.canvas.winfo_rootx() + self.body.radius
        y0 -= self.canvas.winfo_rooty() + self.body.radius
        
        self.body.move(x0,y0)
        
        self.canvas.coords(self.main_line, [self.width,self.width,x0+self.body.radius,y0+self.body.radius])
        
        self.calc_Lpoints()
        
        self.change_orbit()
        
        self.canvas.coords(self.l2_line, [self.body.pos.x,self.body.pos.y,self.l2.pos.x-self.l2.radius,self.l2.pos.y-self.l2.radius])
        
        for point, line in zip([self.l3, self.l4, self.l5],[self.l3_line, self.l4_line, self.l5_line]):
            _fix_line(point, line)


def main():

    app = App()
    app.start()
    
if __name__ == '__main__':
    main()