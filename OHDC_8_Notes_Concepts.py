#functions take a set of instructions, package them together, and attached to a callable name within a given program. 

#review
#create a function called greet().
# 3 pritn statements inside the function
# call function and run

from math import ceil


def greet():
    print("Hello!")
    day = input("Did you have a good day at work? Yes or No?\n")
    if day == 'Yes':
        print("Yaaaaay")
    else:
        print("I'm sorry to hear that, let's do something fun!")

#every time the function is called it will repeat the same series of codes. 
#greet()

#how can we change functions to be more adaptive? 

# function parentheses can contain varaibles, arguments, or other inputs that change the nature of the function.
# inputs are passed into the function to perform a series of tasks. A change in input changes the perspective output. 

#we can create a function that takes an input

def greet_with_name(name):
    print(f'Hello {name}!')
    print(f'How do you do today {name}?')


#calling the function makes python search for the declared function within the file/library/module.  
#required information can then be passed directly into the function itself to change the output. 
#greet_with_name("Jack")

#def my_function(something) > something:the parameter > value: the argument 
# my_function(123) > something = 123  
# argument is the actual piece of data being passed along into the function 
# parameter is the name of that data. It is referenced by name within the function so that tasks can be performed. 

#functions with more than one input
def greet_with(name,location):
    print(f"Hello {name}")
    print(f"How is the weather in {location} today?")

#greet_with("Collin", "Stanwood")

#positional arguments change the data passed based on the position within the parentheses. 
#my_function(a,b,c) > ...(1,3,2) > a = 1, b = 3, c =2 
#if that is rewritten to ...(1,2,3) > a = 1, b = 2, c =3 
# value positioning needs to MATCH the parameter positioning. 

#key word arguement: passing the argument directly by setting it equal to a parameter. 
#makes each line of code longer. However, it makes it less error prone. 
#positional vs keyword can frequently come back to what is required within the application. 
  
def greet_with_2(name, location):
    print(f"Hello {name}")
    print(f"How is the weather in {location} today?")

greet_with_2(name= "Collin", location="Stanwood")

#excercise 1 
#find out the amount of paint required to paint a provided surface area
def paint_calc(height,width,cover):
    cans = ceil((height*width)/cover)

    print(f"You'll need {cans} cans of paint.")

#
test_h = 20
test_w = 25
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#excercise 2
#find if a number is a prime number
#prime numbers ONLY exist when the number is divisibile by itself and by one
#in a given range find if the mod result of n % i is equal to zero.  

#solution one
def prime_checker(number):
    #zero and one are not prime numbers
    if number > 1:
        #starting with a varible is_prime set to True. 
        is_prime = True
        #looping over the range of number -1 because we want to look for any numbers that aren't one or the number itself.
        for i in range (2, number-1):
            print(i)
            #if number mod i(range number) == zero set is_prime to false (because it isn't divisible only by itself and one) 
            if number % i == 0:
                is_prime = False
                #breaks out of loop if we've found a number that make the mod result equal to zero.
                break
            #otherwise pass to the next i value.
            else:
                pass

    #if is_prime remains true for this number, it is a prime number
    if is_prime:
        print("It's a prime number.")

    #otherwise, it is not a prime number.
    else:
        print("It's not a prime number.")
n = int(input("Check this number: "))
prime_checker(number=n)


#solution 2 -> look for number values that exist in the first half of number. 
#if no solution exists number is prime. 
def prime_checker(number):
    #zero and one are not prime numbers
    if number > 1:
        #starting with a varible is_prime set to True. 
        is_prime = True
        #looping over the range of number -1 because we want to look for any numbers that aren't one or the number itself.
        for i in range (2, int(number/2)):
            print(i)
            #if number mod i(range number) == zero set is_prime to false (because it isn't divisible only by itself and one) 
            if number % i == 0:
                is_prime = False
                break
            #otherwise pass to the next i value.
            else:
                pass

    #if is_prime remains true for this number, it is a prime number
    if is_prime:
        print("It's a prime number.")

    #otherwise, it is not a prime number.
    else:
        print("It's not a prime number.")
n = int(input("Check this number: "))
prime_checker(number=n)