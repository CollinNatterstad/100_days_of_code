#turtle module notes and concepts
#documentations works through the contents of a given package and explains its use. 
#documentation should be referenced. google searches can bring up alternative resources as well. 
#packages that are stored with Python can be referenced without downloading.
#otherwise they need to be downloaded and installed within the environment you're working in. 
#if it isn't standard this is required.

import turtle as t
import random

timmy = t.Turtle()

#methods that impact the shape of our dot
#calling shape method to change shape
timmy.shape("turtle")
#calling color method to change color. 
timmy.color("green")

#movement modules. 
timmy.forward(100)
timmy.left(100)
timmy.forward(100)
timmy.left(100)

#tuple in python
#tuple is NOT MUTABLE

tuple = (1,2,4)

t.colormode(255)

def random_color():
    r = random.randint(0,256)
    g = random.randint(0,256)
    b = random.randint(0,256)

    color_t = (r,g,b)
    return color_t

color = random_color

timmy.color(random_color())

screen = t.Screen()
screen.exitonclick()