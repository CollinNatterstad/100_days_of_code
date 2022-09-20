#create a choose your own story game using if statements and predetermined criteria. Don't worry about catching errors or alternative options. 

print("Welcome to Treasure Island.\nYour Mission is to find the treasure.")

cross_road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")

if cross_road == 'left':
    lake = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")

    if lake =='wait':
        house = input('You come up to a house on the island. There are three doors red, blue, and yellow. Please choose a door. (Type red, blue, or yellow)')
        if house == 'yellow':
            print("Congrats! You've won the game!")

        elif house == 'red':
            print('The room is on fire and you become trapped. Game Over')
        
        elif house == 'blue':
            print('The room is full of water and you drown. Game Over')
    else: 
        print("You get a cramp during the swim and drown. Game over.")

else:
    print("Your turn puts you in front of moving vehicle. Game Over.")