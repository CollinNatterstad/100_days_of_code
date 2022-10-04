#scope is the position of an object within python from the most global to the most local one
#example

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function:{enemies}")

#local scope exists within a function
#things ONLY exist in that function. They cannot be accessed outside of the function unless they are a global scope function.

#global variable
player_health = 10

def drink_potion():
    #local variable
    potion_strength = 2

#namespace is valid in specific scopes of a program. The name space provides access to contents within a specific scope.
#there is no block scope in python

game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

        #this has to be within the function scope in order to access new enemy variable. Specifically the if block scope
        #it does not count as a seperate local scope. 
    print(new_enemy)

#modifying a global scope variable in a function.


def increase_enemies_global():
    #you shouldn't use global frequently. It is confusing, and can lead to bugs and errors within the code where global entities are modified over the course of use.
    global enemies 
    enemies += 1
    return enemies

#increase_enemies_global()
#print(f"Enemies Outside of Function: {enemies}")

#global constants
#useful components that are referenced throughout an application or program that are never changed but are consistently interacted wtih. 
#global constants are notorized with an all UPPERCASE format. 

PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@yu_angela"

