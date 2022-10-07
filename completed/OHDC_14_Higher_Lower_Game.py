import random
higher_lower = {
    "John":9,
    "Kelly":17,
    "Aly":1,
    "Chris":18,
    "Charlie":4,
    "James":9,
    "Zena":26,
    "Killorn":11,
    "Yara":25,
    "Xil":24,
    "Tanner":21,
    "Collin":12,
    "Kronk":16,
    "Alex":23,
    "Beti":30,
    "Charon":20,
    "Craig":5,
    "Minx":8,
    "Jayme":31,
    "Carrie":29,
    "Gabe":22,
    "Aaron":45,
    "Sasha":58,
    "Kelsey":3,
}

#selecting a random name from the list in the dictionary
def random_choice(dict,choice_a):
    #flag to trip when condition met
    try_again = True
    while try_again:
        # assign value to the variable
        choice_b = random.choice(list(higher_lower))
        
        #if choice_a and b don't match return choice_b
        if choice_a != choice_b:
            try_again = False    
            return choice_b


#returning the choice with more wins. 
def compare(choice_a,choice_b):
    if higher_lower[choice_a] > higher_lower[choice_b]:
        return choice_a
    else:
        return choice_b

#This is going to ensure that user input is one of the two provided option. repeat test fails when an option is selected and the choice itself is returned. 

def user_choice_check(choice_a,choice_b):
    
    #flag to trip when condition is correct.
    repeat = True
    while repeat:
        user_choice = input("Who do you think has more wins?\n").title()
    
        if user_choice != choice_a and user_choice != choice_b:
            print("Please ensure you've entered the name correctly.")
        
        #returning choice instead of value to ensure no issues with dictionary key. 
        elif user_choice == choice_a:
            repeat = False
            return choice_a

        elif user_choice == choice_b:
            repeat = False
            return choice_b

def game():
    print("\nWelcome to the higher or lower game!\n")
    print("Two choices will be presented.\nPlease select the name you think has the most Rock-Paper-Scissors wins.")

    choice_a = random.choice(list(higher_lower))
    count = 0
    carry_on = True
    while carry_on:
        
        choice_b = random_choice(higher_lower,choice_a)
        print(f"\nYour two choices are: {choice_a} or {choice_b}")
        
        user_choice= (user_choice_check(choice_a=choice_a,choice_b=choice_b))

        winner = compare(choice_a=choice_a,choice_b=choice_b)
     
        if user_choice == winner:
            count += 1
            print(f"\nCongrats! You've won this round.\nYour current score is: {count}")
            choice_a = choice_b

        else:
            print("Sorry, you've selected the wrong person!")
            print(f"You're final score is {count}")
            carry_on = False

game()