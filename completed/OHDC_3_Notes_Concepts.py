#conditional flow statements allow the programmer to determine the course of action based on predetermined criteria

#if else 
#essential idea if condition is true -> do thing a otherwise (else) do thing b

age = 15

#criteria needs to be tabbed in so the computer understands what happens for a given condition
if age >= 16:
    print('older')
else:
    print('Younger')

#criteria can utilize comparitors
# x> , x<, x>=, x<=, x == , x!=

#modulo operation- divides one number by another and provides the remainder of the function

#excercise one

input = 15

if input%2 == 0:
    print('This is an even number.')
else:
    print('This is an odd number')

#nested if statements can build additional criteria into the flow chart

input = 15

if input%2 == 0:
    print('This is an even number.')
    if input >= 14:
        print('This is greater or equal to 14')
    else:
        print('This is smaller than 14.')
else: 
    print('This is an odd number.')

#elif statements allow for additional if components

height = 125
age = 11
if input <= 120:
    print('You can ride this rollercoaster')
    if age <12:
        print("That will be 5 Dollars")
    elif age <=18:
        print('That will be 12 Dollars')
    else:
        print('That will be 7 dollars')
else:
    print("Sorry you can't ride this ride.")

#excercise 2
height = 1.2
weight = 35

bmi = round(weight/height**2,0)
bmi_flat = int(bmi)
if bmi < 18.5:
    print(f'Your BMI is {bmi_flat}, you are underweight.')
elif bmi > 18.5 and bmi < 25:
    print(f'Your BMI is {bmi_flat}, you have a normal weight.')
elif bmi >25 and bmi < 30:
    print(f'Your BMI is {bmi_flat}, you are slightly overweight.')
elif bmi > 30 and bmi <35: 
    print(f'Your BMI is {bmi_flat}, you are obese.')
else:
    print(f'Your BMI is {bmi_flat}, you are clinically obese.')

#excercise 3 - leap year or not leap year
#conditions
#leap when evenly divisible by 4 (except when divisible by 100), unless also divisible by 400. 

year = 2016

if year % 4 == 0:
    if year % 100 ==0: 
        if year % 400 == 0:
            print('Leap year.')
        else:
            print('Not leap year.')
    else:
        print('Leap year.')
else:
    print('Not leap year.')
        
#exercise 4
#method one. There is a better way. 
size = 'M'
add_pepperoni = 'N'
extra_cheese = 'Y'

price = 0 

if size == 'S':
    price += 15
    if add_pepperoni == 'Y':
        price +=2
        if extra_cheese == 'Y':
            price += 1
        else:
            pass
    elif extra_cheese == 'Y':
        price +=1
    else:
        pass

elif size == 'M':
    price += 20
    if add_pepperoni == 'Y':
        price +=3
        if extra_cheese == 'Y':
            price += 1
        else:
            pass
    elif extra_cheese == 'Y':
        price +=1
    else:
        pass
elif size == 'L':
    price += 25
    if add_pepperoni == 'Y':
        price +=3
        if extra_cheese == 'Y':
            price += 1
        else:
            pass
    elif extra_cheese == 'Y':
        price +=1
    else:
        pass
print(f'Your final bill is: ${price}.')

#method 2 - This utilizes a feature I was unaware of. For the code, If blocks will run their own conditional context before running to the next conditional context.
#if one -> size of pizza
#if two -> pepperoni
#if three -> cheese
#this way is cleaner and allows for each if statement to 'own' a component of the application rather than having layers of nested if statements

size = 'M'
add_pepperoni = 'Y'
extra_cheese = 'Y'

price = 0 

# if -> size
if size == 'S':
    price +=15
elif size == 'M':
    price +=20
elif size == 'L':
    price +=25

#if -> add pep
if add_pepperoni == 'Y':
    if size =='S':
        price +=2
    else:
        price +=3
# if -> extra cheese
if extra_cheese == 'Y':
    price +=1

print(f'Your final bill is: ${price}.')

#adding logical operators to an if statement
# and or not
# and -> both have to be true. otherwise it is false
# or -> one or the other have to be true. otherwise false
# not -> if condition is true -> 

