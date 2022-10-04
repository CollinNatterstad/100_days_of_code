import random

affirm = ['y','yes','yeah','yep']
deny = ['n','no','nah','nope']

def intro():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Please choose a difficulty. Type 'easy' or 'hard':\n").lower()
    return difficulty

def select_difficulty(difficulty):
    chances = 0
    if difficulty == 'hard':
        chances += 5
        return chances

    elif difficulty == 'easy':
        chances += 10
        return chances

def select_number():
    number = random.randint(1,100)
    return number

def check_the_guess(number,guess):

    if number == guess:
        print("You've selected the correct number!")
        return True
    elif number > guess:
        print("You're guess is to low.")
        return False
    elif number < guess:
        print("You're guess is to high.")
        return False

def carry_on():
    carry_on = input("Would you like to keep playing?\n").lower()
    if carry_on in affirm:
        play_game()

    elif carry_on in deny:
        print("Thanks for playing!")
        exit()

def play_game():       
    difficulty = intro()
    chances = select_difficulty(difficulty=difficulty)
    print(f"You have {chances} chances remaining!")
    number = select_number()

    check_guess = False
    while not check_guess and chances > 0:
        guess = int(input("Please enter a number from 1 to 100.\n"))
        check_guess = check_the_guess(number,guess)
        if check_guess:
            carry_on()
        
        elif not check_guess:
            chances -= 1
        print(f"You have {chances} chances remaining.")

        if chances == 0:
            print("You've run out of chances!")
            carry_on()

play_game()