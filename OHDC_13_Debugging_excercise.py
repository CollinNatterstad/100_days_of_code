#excercise one
#original code
#problem is value assignment not value comparison. 
number = int(input("Which number do you want to check?"))

'''if number % 2 = 0:
  print("This is an even number.")
else:
  print("This is an odd number.")'''

#fix is to add an = and make the if statement a comparator not attempt to assign a value. 
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
#excercise 2
#year won't be in int format > needs to be converted to int. 
year = input("Which year do you want to check?")

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

#fix
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

#excercise 3
for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0:
    print("FizzBuzz")
  if number % 3 == 0:
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])

#fix
#changed comparator logic to and not or
#changed seperate if blocks to one if else if block
#changed number from list type to passed variable. 
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)