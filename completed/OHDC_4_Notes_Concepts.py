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

#changes the value for second index place. Index can also be negative as well.
states[2] = 'montana'
print(states)
#last position of string
states[-1] = 'kentucky'

#can also extend the list by adding an addtional list
states.extend(['utah','delaware','rhode island'])
print(states)

#nested lists are lists ofs lists

list1 = ['Joe','bob','tim']
list2 = ['jane','jill','jackie']

#lists owns values within list 1 and 2. Two sets of brackets. 
lists = [list1,list2]



#excercise two: bill roulette. With a list of names select one person at random to pay the bill.  

#establishing a list of names
names = ['bob','joe','jill','jane','tim']

#generating a random number from position 0 (bob) to one less than than the total maximum count (because 0 counts as a digit)
number = random.randint(0,len(names)-1)

#passing two variables at the same time. First is the name at the index of number. Not matter how long the list is it will pull the name for that position. 
print(f"{names[number]} is going to buy the meal today!")

#excercise 3
#creating the intital playing board 
#assuming that players won't pick a position out of 1-3 columns and rows.

#three seperate lists
row1 = ["","",""]
row2 = ["","",""]
row3 = ["","",""]

#list of lists are stored to map variable
map = [row1, row2, row3]

#position is typically provided as an input but this is convenient. 
position = '23'

#two variables 1. stores column value, 2. stores row value. This is gained by indexing the position string, converting it to an int and subtracting one to establish
#python appropriate index position. failure test here would involve looking for values where x > 3 and x < 0 
column = (int(position[0]))-1
row = (int(position[1]))-1

#calls the list of list by finding the row first(the appropriate list). Then finding the column (the index wtihin that row.))
map[row][column]='x'

#prints an f string making the board more realistic. 
print(f'{row1}\n{row2}\n{row3}')
