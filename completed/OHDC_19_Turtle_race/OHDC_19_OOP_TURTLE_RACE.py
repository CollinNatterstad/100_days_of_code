import random
import turtle as t


class RaceTurtles:

    def __init__(self,name,color,y_cord):
        self.name = name
        self.turtle = t.Turtle()
        self.turtle.penup()
        self.turtle.shape('turtle')
        self.set_color = self.turtle.color(color)
        self.color = color
        self.y_cord = y_cord
        self.x_cord = -230
        self.position = self.turtle.goto(x=self.x_cord,y=self.y_cord)
        self.winner = False
        self.count = 0

class RaceCohort:

    def __init__(self):
        self.turtle = [
        RaceTurtles(name='tom',color='red', y_cord= 100),
        RaceTurtles(name='tim',color='green', y_cord = 50),
        RaceTurtles(name='tara',color='blue',y_cord=0),
        RaceTurtles(name='nick',color='black',y_cord=-50),
        RaceTurtles(name='rico',color='pink',y_cord=-100)
        ]

    def there_is_winner(self,x_cord):
        if x_cord >= 230:
            return True

    def race(self):
        carry_on = True
        while carry_on:
            for item in self.turtle:
                if self.there_is_winner(item.x_cord):
                    item.winner = True
                    carry_on = False
                    break                    
                    
                else:
                    movement = random.randint(10,50)                   
                    item.turtle.forward(movement)
                    item.x_cord += movement

    def find_winner(self):
        for item in self.turtle:
            if item.winner == True:
                return item.color

    def compare_bet_winner(self,bet):
        
        if self.find_winner() == bet:
            print("Yaaaay")
        else:
            print("You didn't pick the right turtle")

screen = t.Screen()
screen.setup(width=800,height=500)
bet = screen.textinput(title="Place your bet",prompt="Which turtle will win the race?")

race = RaceCohort()
race.race()

winner = race.compare_bet_winner(bet=bet)  

screen.exitonclick()




