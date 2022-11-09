'''
For pong we are going to need a playing field.
the field has...
    1. Dashed Centerline 
    2. Two Scoreboards left/right of center

scoreboard class
    1. spawns at a location
    2. changes score with each 'goal' 

'ball' class
    1. spawns at 0,0
    2. moves at 45 degree to contact intiation
    3. recognizes going 'through' the goal post. 

paddle class
    1. spawns at field ends.
    2. moves up and down the field 

game 
    1. spawn the ball in.
    2. while ball is alive game plays. 
    3. when ball is not alive game resets while player totals are less than 0
'''
import turtle as t
from random import choice
import time

height = 600
width = 1000

score_pos = [(-50,150),(50,270)]

ball_direction = [0,180]

class ScoreBoard():
    def __init__(self):
        
        self.left_score = 0
        self.right_score = 0
        self.create_left_score()
        self.create_right_score()

    def create_left_score(self):
        self.left_board = t.Turtle
        self.left_board.hideturtle()
        self.left_board.penup()
        self.left_board.color('white')
        self.left_board.setposition(x=-50,y=270)
        self.update_score()
        
    def create_right_score(self):
        self.right_board = t.Turtle
        self.right_board.hideturtle()
        self.right_board.penup()
        self.right_board.color('white')
        self.right_board.goto(x=50,y=270)
        self.update_score()

    def increase_left_score(self):
        self.left_score += 1
        self.left_board.clear()
        self.update_score()

    def increase_right_score(self):
        self.right_score += 1
        self.right_board.clear()
        self.update_score()

    def update_score(self):
        self.left_board.write(self.left_score,font = ('Arial',20,'normal'))
        self.right_board.write(self.right_score,font = ('Arial',20,'normal'))

class PlayingField(t.Turtle):
    def __init__(self):
        super().__init__()
        self.dashed_line()
   
    def dash(self):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

    def dashed_line(self):
        self.hideturtle()
        self.left(90)
        self.pencolor('white')
        self.penup()     
        self.setposition(0,-300)
        
        for step in range(30):
            self.dash()
        
class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.shapesize(.5)
        self.penup()
        self.in_play()
    
    def in_play(self):
        self.clear()
        self.home()
        self.setheading(choice(ball_direction))
        self.forward(20)

#setting up the screen.
screen = t.Screen()
screen.setup(width=1000,height=500)
screen.bgcolor('black')
screen.title('Pong!')
screen.tracer(n=1)

time.sleep(.01)

score_board = ScoreBoard()
field = PlayingField()
ball = Ball()

game_on = True

while game_on:

    screen.update()
    time.sleep(.01)


screen.exitonclick()  