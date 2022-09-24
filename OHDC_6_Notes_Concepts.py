#format of a function
#function name then () > print(variable) where print is the function name and variable is the argument or task passed in to be completed. 

#creating a variable
#def > defining > establishing what a given function will do / what arguments it will take. 

def function():

    #contents provide the algorithmic steps by which the function completes an objective. 
    print("hello")
    print("bye")


#a function has to be called in order to work. 
#this calls the contents / arguments of the function and proceeds through them. 
#ctrl + ] does a group indent right ctrl + [ does indent left. 
function()

#indentation scope determines the hierarchy of code and when things are subsequently run. 
#code furthest to the left is the higest governing code that is run first. Code indented right is run in decreasingly lower hierarchy

#code works left to right > calls to the function block 

#the function block
def function2(value):
    #what the function block does
    if value >= 2:
        #what the conditional block does. 
        print("Yaaaay")
    else:
        print("Booooo")

#function is called with an explicit number.
function2(3)

#for loop has two variations using the same for in sequence

#for items in variable:
#and
#for items in range:


#while loop > looping function that exists while a condition is true.

count = 0 

#while the count is less than or equal to 10...
while count <=10:
    #add 1 to the count with each loop until 10. 
    count +=1 

#check count > if less/equal to 10 > add one > repeat.

#for loops are great for iteration
#while loops are great when you're not sure how many iterations will take place. 

#hurdle challenge on reeborg's world

#functionality to catch. 
#need to know when there is a wall in front of us. and a wall to our right. when we are at the top of a wall. when we are at the bottom of a wall. 

#function calls are functions that exist within reeborg's world. 
'''def turn_right():
    turn_left()
    turn_left()
    turn_left() 

def top():
    turn_right()
    move()
    turn_right()

def turn_around():
    turn_left()
    turn_left()

while not at_goal():
    if wall_in_front() == True:
        turn_left()
        while wall_on_right() == True:
            if wall_in_front() == True:
                turn_left()
            else:
                move()
            if wall_on_right() != True:
                top()
    if wall_in_front() != True:
        move()
'''