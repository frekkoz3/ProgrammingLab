import turtle
turtle.colormode(255)
import random
import time

class RGBColor:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

class RandomRGBColor(RGBColor):
    def __init__(self):
        self.red = random.randint(0, 255)
        self.green = random.randint(0, 255)
        self.blue = random.randint(0, 255)

class Pixel():
    def __init__ (self):
        pass
        
    def draw(self, color, t, dim):
        
        red = color.red
        green = color.green
        blue = color.blue

        t.pencolor(red, green, blue)
        t.begin_fill()
        t.fillcolor(red, green, blue)
        
        for i in range (4):
            t.forward(dim)
            t.left(90)
            
        t.end_fill()
        
class Square:
    def __init__(self, lato):
        self.lato = lato

    def drawrandomrquare(self):
        
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)

        for i in range (self.lato):
            for j in range (self.lato):
                t.up()
                t.goto(i*5, j*5)
                t.down()
                
                p = Pixel()
                color = RandomRGBColor()
                p.draw(color, t, 5)
                
        time.sleep(10)  
        t.bye()

    def drawredvariantsquare(self):
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)

        randomcolor = RandomRGBColor()
        color = RGBColor(0, randomcolor.green, randomcolor.blue)
        
        for i in range (self.lato):
            for j in range (self.lato):
                t.up()
                t.goto(i*5, j*5)
                t.down()
                
                p = Pixel()
                p.draw(color, t, 5)
                color.red = color.red + 1
                
        time.sleep(10)  
        t.bye()

    def drawgreenvariantsquare(self):
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)

        randomcolor = RandomRGBColor()
        color = RGBColor(randomcolor.red, 0, randomcolor.blue)
        
        for i in range (self.lato):
            for j in range (self.lato):
                t.up()
                t.goto(i*5, j*5)
                t.down()
                
                p = Pixel()
                p.draw(color, t, 5)
                color.green = color.green + 1
                
        time.sleep(10)  
        t.bye()

    def drawbluevariantsquare(self):
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)

        randomcolor = RandomRGBColor()
        color = RGBColor(randomcolor.red, randomcolor.green, 0)
        
        for i in range (self.lato):
            for j in range (self.lato):
                t.up()
                t.goto(i*5, j*5)
                t.down()
                
                p = Pixel()
                p.draw(color, t, 5)
                color.blue = color.blue + 1
                
        time.sleep(10)  
        t.bye()

    def drawgrayvariantsquare(self):
        t = turtle.Turtle()
        t.hideturtle()
        t.speed(0)

        color = RGBColor(0, 0, 0)
        
        for i in range (self.lato):
            for j in range (self.lato):
                t.up()
                t.goto(i*5, j*5)
                t.down()
                
                p = Pixel()
                p.draw(color, t, 5)
                color.red = color.red + 1
                color.green = color.green + 1
                color.blue = color.blue + 1
                
        time.sleep(10)  
        t.bye()
         
square = Square(16)
square.drawgrayvariantsquare()