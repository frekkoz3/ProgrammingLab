import turtle
import random
import time

class RandomColor:
    
    def __init__(self):

        colori = [ 'white', 'black']
        #colori = ['black', 'cyan', 'magenta', 'yellow', 'white', 'red']
        i = random.randint(0,len(colori)-1)
        self.color_name = colori[i]

class Pixel:
    
    def __init__ (self):
        
        pass
        
    def draw(self, color, turtle_t, side):

        turtle_t.pencolor(color.color_name)
        turtle_t.begin_fill()
        turtle_t.fillcolor(color.color_name)
        
        for i in range (4):
            turtle_t.forward(side)
            turtle_t.left(90)
            
        turtle_t.end_fill()

class Square:

    def __init__(self, side, pixel_dim):
        
        self.side = side
        self.pixel_dim = pixel_dim

    def draw(self):
        
        t = turtle.Turtle()
        screen = turtle.Screen()
        screen.bgcolor("green")
        t.hideturtle()
        t.speed(0)

        for i in range (self.side):
            
            for j in range (self.side):
                
                t.up()
                t.goto(i*self.pixel_dim, j*self.pixel_dim)
                t.down()
                
                p = Pixel()
                color = RandomColor()
                p.draw(color, t, self.pixel_dim)

        time.sleep(3)


for i in range (100):
    random_square = Square(3, 5)
    random_square.draw()
