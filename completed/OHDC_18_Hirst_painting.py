import turtle as t
import random

t.colormode(255)

dot = t.Turtle()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    color_t = (r,g,b)
    return color_t    

#10 step by 10 step grid.
# Set coords @ origin
# Moving right 10 steps. Return to x = 0. y + 50 repeat. 
#dots are 20 in size
#spaced by 50 paces.
#color is random

def moving_dots():
    dot.home()
    height = 0

    def move_out():
        for step in range (10):
            dot.penup()
            dot.pencolor(random_color())
            dot.dot(20)
            dot.forward(50)
            
    def move_up(height):
        height += 50
        return height

    for steps in range(10):
        move_out()
        #setting height to the move up function > returns the height plus 50 of each step
        height = move_up(height)
        #height resets at x cord 0, y cord of height plus 50
        dot.setpos(0,height)

moving_dots()
screen = t.Screen()
screen.exitonclick()