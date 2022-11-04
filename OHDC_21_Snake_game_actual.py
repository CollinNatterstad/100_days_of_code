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

class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(.5)
        self.speed(0)
        self.color('pink')
        self.shape('circle')
        self.refresh()
    
    def refresh(self):
        rand_x = random.randint(-270,270)
        rand_y = random.randint(-270,270)

        self.goto(rand_x,rand_y)

#creates single unit of snake chain. 
class SnakeSection: 

    def __init__(self):
        self.section = t.Turtle()
        self.section.shape('square')
        self.section.color('white')
        self.section.penup()
        self.food = 0
        
class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snek()
        
        self.head = self.segments[0]
        self.tail = self.segments[-1]

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
        new_segment = SnakeSection()
        new_segment.section.goto(self.tail.section.pos())
        self.segments.section.food += 1
        # self.segments.append(new_segment)
        # self.tail = self.segments[-1]

class Scoreboard(t.Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.setposition(x=0,y=270)
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.write(f'Score: {self.score}',align='center',font = ('Arial',20,'normal'))
    

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        

#the game itself.

screen = t.Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.snek_up, 'w')
screen.onkey(snake.snek_down,'s')
screen.onkey(snake.snek_left,'a')
screen.onkey(snake.snek_right,'d')

game_on = True

while game_on:
    
    screen.update()
    snake.move_snek()
    
    if snake.head.section.distance(food.pos()) <= 15:
        food.refresh()
        
        #snake.add_section()

screen.exitonclick()