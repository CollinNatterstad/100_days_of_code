''' These commands call functions within the Reeborg's World application. 

create a program that will traverse the maze. 

What I need to know. 
If there is a wall ahead (or isn't)
if our right is clear or not

The hint is that the robot must follow the right edge of the map to the end destination


right_is_clear > right shoulder is unobstructed
wall_on_right > right shoulder on wall

front_is_clear > nothing in way. 
wall in front > heading into wall

when nothing is in front of us we move forward. 

a right move requires the right to be open, we turn right and move once. 
if the front is open we move once
if there is no other option we turn left. 

until we have a wall on the right side of the robot we need to move it in space until it reaches a wall. turning it left places the right
shoulder on the wall. 

def turn_right():
    turn_left()
    turn_left()
    turn_left() 

while front_is_clear():
    move()
turn_left()

while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()
'''