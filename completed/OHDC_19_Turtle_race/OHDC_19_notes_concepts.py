from turtle import Turtle, Screen
timmy = Turtle()
screen = Screen()
#creating a funciton that we call within another function
def move_forward():
    timmy.forward(100)

#listen function looks for user input, flags when it occurs.
screen.listen()
#when a specific action occurs we pass the function parameter in > when this happens > this occurs.
screen.onkey(key="space",fun=move_forward)#no () are used in the function call in this case. assumption. no inputs required in the actual function itself.

#the process of passing one function into another introduces the concept of higher order functions
#Function that works with other functions. 
#takes function as inputs which is common in python when you need to call a specific function under a specific event. 

#def add(n1,n2)

#def calc(n1,n2,function):
    #function(n1,n2)

#passed one function into another. 
#calc(n1,n2,add)

#object vs class
#timmy = Turtle()

#instances of the same object interact differently
#These are both instances of the turtle class. 
#timmy = Turtle()
#tommy = Turtle()

#keeps screen open
screen.exitonclick()