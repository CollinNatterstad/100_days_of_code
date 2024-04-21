import turtle as t
import pandas as pd

def game_loop(t = t.Turtle()):
    df = pd.read_csv('\OHDC_25\\50_states.csv')
    while True:
        if len(df.state) == 0:
            t.penup()
            t.home()
            t.pendown()
            t.write("You Win!")
            False
        state_guess = screen.textinput(title= 'Guess A State.',  prompt= 'Please Enter A State').title()
        if len(df[df.state==state_guess]) == 1:
            dfx = df[df.state==state_guess]
            state, x, y = dfx.iloc[0]["state"], dfx.iloc[0]["x"], dfx.iloc[0]["y"]
            t.color("white")
            t.penup()
            t.goto(x,y)
            t.pendown()
            t.color("black")
            t.write(state,move=False,align="left")
            df = df.drop(df[df.state==state_guess].index)

screen = t.Screen()
screen.title("U.S. State Guessing Game")
image = "D:\Coding Projects\\100 Days of Code\OHDC_25\\blank_states_img.gif"
screen.addshape(image)
t.shape(image)
game_loop()
screen.exitonclick()
t.mainloop()

# # '''
# # components of challenge
# # 1. check the guessed answer against the list of items in df.
# #     > only one row per state. 
# # 2. write state name at coordinate when correct
# # '''