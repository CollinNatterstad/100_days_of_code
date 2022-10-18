import turtle as t
import random
#can be written as from turtle import * > from turtle import all
#can also alias the module name
#from turtle as t > allows you to reference the name as t not turtle. 

#make a square
dot = t.Turtle()
t.colormode(255)

# #simple way
# dot.forward(100)
# dot.left(90)
# dot.forward(100)
# dot.left(90)
# dot.forward(100)
# dot.left(90)
# dot.forward(100)

# #better way
# for steps in range(4):
#     dot.forward(100)
#     dot.left(90)

#challenge 2 draw a dashed line. 
#steps of 10 paces colored then not colored

# for steps in range(10):
#     dot.pendown()
#     dot.forward(10)
#     dot.penup()
#     dot.forward(10)

#challenge 3: draw other shapes.
#draw a triangle, square, pentagon, hexagon,heptagon, octagon, nonagon, and decagon so that they are overlayed

#sides + 1 > angle changes with each addition. 

#function that takes sides as parameter
# def make_shape(sides):
#     colors = ['red','blue','green','purple','grey','black','orange','charcoal']
    
#     #divides the exterior angle by total number of sides
#     ext_angle = 360/sides
#     dot.color(random.choice(colors))
#     #for each side of a given shape it steps forward then rotates by the exterior angle to the left. 
#     for side in range(sides):
        
#         dot.forward(100)
#         dot.left(ext_angle)

# #loops through all sides and makes a new shape.
# for sides in range(3,25):
#     make_shape(sides)
#challenge 4 draw a random walk. 
#for movements north south east west. same increments. randomly chooses color as it walks

# def random_walks(steps):
#     def random_color():
#         r = random.randint(0,256)
#         g = random.randint(0,256)
#         b = random.randint(0,256)

#         color_t = (r,g,b)
#         return color_t    
    
#     dot.pensize(5)
#     dot.speed(8)
#     turn_angle = [0,90,180,270]


#     for steps in range(steps):
#         dot.color(random_color())
#         dot.setheading(random.choice(turn_angle))
#         dot.forward(20)

# steps = 1000       
# random_walks(steps)

#challenge 5 spirograph
#make a circle that is rotating by a determined angle. 

def spirograph(steps):
    def random_color():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        color_t = (r,g,b)
        return color_t

    angle = 360/steps

    for step in range(steps):
        dot.speed(0)
        dot.color(random_color())
        dot.circle(200)
        dot.left(angle)

steps =93
spirograph(steps)


screen = t.Screen()
screen.exitonclick()