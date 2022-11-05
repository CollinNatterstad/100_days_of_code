import random
import turtle as t
import time

starting_position = [(0,0),(-20,0),(-40,0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0

#typically classes are hosted in other files, they're kept in this file simply for convenience.
class Food:
    def __init__(self) -> None:
        self.body = t.Turtle()
        self.body.penup()
        self.body.shape('circle')
        self.body.color('pink')
        self.body.shapesize(.5)

    def place_random_food(self):
        self.foodx_cord = random.randint(-270,270)
        self.foody_cord = random.randint(-270,270)      
        self.foodposition = self.body.goto(self.foodx_cord,self.foody_cord)
        return self.body.pos()

#creates single unit of snake chain. 
class SnakeSection: 

    def __init__(self):
        self.section = t.Turtle()
        self.section.shape('square')
        self.section.color('white')
        self.section.penup()
        
class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snek()
        self.head = self.segments[0]

    def create_snek(self):
        for item in starting_position:
            new_segment = SnakeSection()
            new_segment.section.goto(item)
            self.segments.append(new_segment)

    def move_snek(self):
        
        #provides the index number to pass in.
        #we're not actually LOOPING through the group of objects. 
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].section.xcor()
            new_y = self.segments[seg_num-1].section.ycor()
            
            self.segments[seg_num].section.goto(new_x,new_y)
        self.head.section.forward(move_distance)

    def snek_up(self):
        if self.head.section.heading() != down:
            self.head.section.setheading(90)

    def snek_down(self):
        if self.head.section.heading() != up:
            self.head.section.setheading(270)

    def snek_right(self):
        if self.head.section.heading() != left:
            self.head.section.setheading(0)
    
    def snek_left(self):
        if self.head.section.heading() != right:
            self.head.section.setheading(180)

    def add_section(self):
        pass

class Game:

    def __init__(self) -> None:
        pass


#the game itself.

screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer()

snake = Snake()

screen.listen()
screen.onkey(snake.snek_up, 'w')
screen.onkey(snake.snek_down,'s')
screen.onkey(snake.snek_left,'a')
screen.onkey(snake.snek_right,'d')

game_on = True

while game_on:
    
    screen.update()
    time.sleep(.01)
    
    snake.move_snek()
    
screen.exitonclick()