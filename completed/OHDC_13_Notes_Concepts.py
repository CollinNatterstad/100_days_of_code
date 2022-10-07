#debugging code

#finding and debugging code.

#Tips to debugging
#1. describe problem 
#2. reproduce the bug. Find when the bug is triggered in the code.
#3. evaluate each line 
#4. Fix the errors 
#5. Print is your friend during debugging
#6. Use Debugger -> runs code line by line. Shows how the code is being implemented during the course of a day. 
#7. Take a break.
#8. Ask a friend
#9. Run the code often. -> confirm functionality before moving on. Tackle bugs one at a time.
#10. Research on stackover flow. 

# example one
#what is going wrong. 
#the code won't work in this fashion because range(1,20) includes one but NOT 20. i != 20; i doesn't print the appropriate string. 
def my_function():
    for i in range(1,20):
        if i == 20:
            print("You Got it")

my_function()

# this will work now. 
def my_function2():
    for i in range(1,21):
        if i == 20:
            print("You Got it")

#supplied problem.
#idea, the dice_num index operates in range 1-6 while the string list operates through index 0-5.
#Bug will rear it's head when the index position is 6 which won't exist in the str list.

from random import randint
dice_num_str = ["1","2","3","4","5","6"]
dice_num = randint(1,6)
print(dice_num_str[dice_num])

#the fix without interacting with rand int. 
print(dice_num_str[dice_num-1])
#alternative fix that changes range
#dice_num = randint(0,5)


#original code
#issue, code not outputting when year == 1984
# use of non-inclusive logic. < than but not equal to. 
year = int(input("What's your birth year?\n"))
if year >1980 and year <1994:
    print("You are a millenial.")
elif year > 1984:
    print("You are a Gen Z")

#fix > make inclusive by adding less than or equal to 1994. 
year = int(input("What's your birth year?\n"))
if year > 1980 and year <= 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z") 

#original code.
#problem inputput isn't int > type error 
age = input("How old are you?")
if age > 18:
    print("You can drive at age {age}")

#fix > input type for comparator. f string fix to change to pass in the variable. 
age = int(input("How old are you?\n"))
if age > 18:
    print(f"You can drive at age {age}")


#issue, word_per_page utilizes a comparator not assignment of a value. 
pages = 0 
word_per_page = 0

pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

#fix is to remove an equal sign and make it assign value to variable. 
pages = 0 
word_per_page = 0

pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

#using debugger
#using this original function the issue stems from location of b_list.append.
#this iteration will only append the last item. Instead, the b_list.append needs to be added to the for-loop
#This ensures that the new list item is appendend with each iteration.  

'''def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item*2
    b_list.append(new_item)
    print(b_list)

mutate (1,2,3,4,5)'''

#fix
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item*2
        b_list.append(new_item)
    print(b_list)

mutate (1,2,3,4,5)