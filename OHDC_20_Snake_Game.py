import random
import turtle as t
import time

starting_position = [(0,0),(-20,0),(-40,0)]
move_distance = 20


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

#creates single unit of 
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

    def create_snek(self):
        for item in starting_position:
            self.body = SnakeSection()
            self.food_eaten = 0
            self.body.section.goto(item)
            self.segments.append(self.body)

    def move_snek(self):
        
        for num in range((self.segments)-1,0,-1):
            new_x = self.segments[num-1]




        #we are passing in a int to pull a specific object at an index. 
        #new_x and y are derived from the x and y cordinates. 
        #this is then passed on to update the current index position and moving to the next one. 
        
        #we need to take the last object and work backwards. or reverse the list order then go forward.

        #passes nonetype error?
        #for index, item in enumerate(self.segments.reverse()):
            #pass
        
        #this doesn't pass with error but can't access object attributes including last xcor/ycor
        # for item in self.segments:
        #     pass

        #adding reverse() creates nonetype error. Runs without. 
        # for item in self.segments.reverse():
        #     pass

        # enumerate now works. likely that reverse doesn't like the objects contained in the self.segments list.
        # for index,item in enumerate(self.segments):
        #     pass

        # for seg_num in range(len(self.segments)-1,0,-1):
        #     new_x = self.segments[seg_num-1].xcor()
        #     new_y = self.segments[seg_num-1].ycor()
        #     self.segments[seg_num]
        
        #     seg_num[0].forward(20)
            
        #     new_x = self.segments[segment -1].xcor()
        #     new_y = self.segments[segment -1].ycor()
        #     segment.body.section.goto(new_x,new_y)
        # self.body.section.forward(20)

    def eat_food(self,impact):
        return self.body.section.pos() == Food().place_random_food()

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
screen.tracer(0)

snake = Snake()

game_on = True
while game_on:
    screen.update()
    snake.move_snek()
    time.sleep(.1)
    screen.exitonclick()