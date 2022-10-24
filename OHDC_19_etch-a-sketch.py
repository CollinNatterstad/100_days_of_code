from turtle import Turtle, Screen, clear

#create an etch-a-sketch app that takes user input to create a result
#w > forwards, s > backwards, a > left, d > right. c> clears drawing

dot = Turtle()
screen = Screen()
dot.speed(0)

def forwards():
    dot.forward(10)
def backwards():
    dot.backward(10)
def left():
    dot.left(10)
def right():
    dot.right(10)   
def clear_turtle():
    dot.clear()


screen.listen()

screen.onkey(key='w',fun=forwards)
screen.onkey(key='s',fun=backwards)
screen.onkey(key='a',fun=left)
screen.onkey(key='d',fun=right)
screen.onkey(key='c',fun=clear_turtle)



screen.exitonclick()