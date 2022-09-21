#import statement allows you to access previously created libraries that expand the functionality within python without having to create it yourself. 
import random

#selecting a random integer. Storing that value and printing it.
random_integer = random.randint(1,10)
print(random_integer)

#returns random float value from 0.00000 - .99999
random_float = random.random()

#multiply float value by an int value to go beyond this.

random_float * 5
print(random_float)

#Excercise 1
#heads or tails

random_choice = random.randint(0,1)

if random_choice == 1:
    print("heads")
else:
    print("tails")


#talking about lists

#list -> data structure: way of organizing and storing data in python. stores a group of data seperated by columns. 
#order and data type don't matter. lists are also mutable so they can be changed. They do not have key:value pairs but are indexed based on their position in the list. 
#order can be a problem without key:value pairs and nested values (as can happen with json content)
#normal pythonic index (starts at 0). Items can be appended to the list (increasing the total index count) or mutated by calling a specific item index within a list

states = ['washington','oregon','california']

#adds an additional item to the list. 
states.append('idaho')

#changes the value for second index place.
states[2] = 'montana'

#can also extend the list by adding an addtional list
states.extend(['utah','delaware','rhode island'])
print(states)