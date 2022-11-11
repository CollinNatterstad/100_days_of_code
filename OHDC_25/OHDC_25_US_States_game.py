import turtle as t
import pandas as pd

df = pd.read_csv('D:\Coding Projects\\100 Days of Code\OHDC_25\\50_states.csv')

def check_state(guess):
    #if the length of the returned value == 1 (e.g. it exists in the column)
    if len(df[df.state == guess]) == 1:
        return True
    else:
        return False

screen = t.Screen()

screen.title("U.S. State Guessing Game")

image = "D:\Coding Projects\\100 Days of Code\OHDC_25\\blank_states_img.gif"
screen.addshape(image)

t.shape(image)

state_guess = screen.textinput(title= 'Guess A State.',  prompt= 'What is another State name')

'''
components of challenge
1. check the guessed answer against the list of items in df.
    > only one row per state. 
2. write state name at coordinate when correct
'''

if check_state(guess=state_guess.title()): 
    
    
    x = df.x
    y = df.y


t.mainloop()