#functions have three forms
#functions that do a specific tasks with contained data.
#functions that perform tasks based on inputed data
#functions that return data after performing tasks with inputed/contained data. 

from os import terminal_size
import string


def my_function():
    #performing a simple calculation 
    result = 3*2
    #returning the variable of the result.
    #can also be written as return 3*2 as well
    return result


#variable is set equal to the function. Python looks at the contents of the function above, and sets my_function = result within the varia variable.
varia = my_function()
print(varia)

#functions with outputs are like a machine. They take (usually) an input or condition, perform the prescribed changes to them, then output the
#appropriate values.

def format_name(first,last):
    #escape condition for when no characters are provided.
    if first == '' and last == '':
        return "No Name is included"

    #assigning inputs to variables 
    f_name = str(first).title()
    l_name = str(last).title()

    #returning a formatted string.
    return f"{f_name} {l_name}"

name = format_name(input("what is your first name?"), input("What is your last name?"))
print(name)

#excercise
#return true or false for if_leap_year.
#return the number of days in a given month

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year,month):
    adjusted_month = month-1
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

    if is_leap(year) == True and adjusted_month == 1:
        return((month_days[1])+ 1)

    else:
        #return function will exit the outter function and prevent code below the return statement (but within the function from running)
        return(month_days[adjusted_month])

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year = year, month = month)
print(days)

#doc strings provide information on what a given function does. Needs to go directly after a declaration for a function.

def my_function():
    #this is a multi-line comment that becomes the doc string
    """doc string that will describe how the function that will work."""

    # alternatively, we can make 
    # a multiline comment by
    # typing our comment then highlighting and pressing ctrl + /
    # to add comment marks.

    a = 'string'
    print(a)

my_function()

#return vs print

# print is a function that will print an element in the terminal
# it cannot be interacted with down stream beyond the print to the terminal
# return by comparison can interact with other functions and the terminal. 
# in this way, when you'd like to have additional functionality provided downstream you can return the approprate data and move it downstream accordingly. 

'''numbers = [0,1,2,3,4,5,6,7,8,9]

def add(n1,n2):
    return n1+n2

def subt(n1,n2):
    return n1-n2

def mult(n1,n2):
    return n1 * n2

def div(n1,n2):
    
    if n2 > 0:
        return n1/n2

    elif n2 == 0:
        return "You cannot divide by zero."

n1 = int(input("What is your first number?\n"))
n2 = int(input("What is your second number?\n"))

operations = {'+':add(n1,n2),'-':subt(n1,n2),'*':mult(n1,n2),'/':div(n1,n2)}

for symbol in operations:
    print(symbol)
operation = input("Choose the symbol of the calculation you'd like to perform.\n")

answer = operations[operation]

print(f'{n1} {operation} {n2} = {answer}')'''

#a recursion loop occurs when a function is called from within the function. 