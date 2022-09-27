# varying data types strings, integers, floats, booleans
#strings
#Only strings can be concatenated. 
string = "string"

#you can pull out specific characters utilizing index position starts with zero -> subscripting, reads left to right 
print(string[0])

#you can access the last character by using -number
print(string[-1])

#integers - whole numbers without decimal places

#can print arthmatic function 
print(123+456)

#underscores can be added to numbers to make them more readable. 

print(123_456)

#float - numbers that contain decimal values

print(3.1459)

#boolean - logical expression that evaluate to true or false

#begin with capital T and Capital F

#True | False

#function is a series of steps that are programmed to take a specific input and conver it into a specific output.  

#type function can help determine what the type of data something is.

print(type(string))

#we can convert between data types so long as they are aligned 
number = '4325'
print(type(number))
new_number = int(number)
print(type(new_number))

#this will work because number is in the form of a string FIRST. print(string+new_number) will not because you cannot concat an integer with a string. It has to be converted
print(string+number)

#excercise one 

input = '42'

a = int(input[0])
b = int(input[1])

print (a+b)

#excercise two

height = "1.6"
weight = "35.6"

aa = float(height)
bb = float(weight)

xx = int(b / (a**2))

print(x)

#number manipulation and fstrings

#round function takes floating point data and rounds them to a specified (or utilze the default) number of decimal places.
print(round(8/3, 2))

#floor division rounds down to the lowest possible integer. 
#syntax with '//'
print(8//3) 

#divide equals syntax lets you short hand divide a variable. This syntax works with other aritmatic functions as well. 
# += -= *=

xxa = 4/2

xxa /= 2

print(xxa)

#fstrings - allow for variable values to be injected into a string with the least amount of effort

score = 0 
height = 1.6
iswinning = True

print(f"Your score is {score}. Your height is {height}. Are you winning {iswinning}")

#exercise three
 
age = 56

max = 90
max_days = max*365 
max_weeks = max*52
max_months = max*12

age_days = int(age)*365
age_weeks = int(age)*52
age_months = int(age)*12

days = max_days-age_days
weeks = max_weeks-age_weeks
months = max_months-age_months

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
