
fruits = ['Apple','Peach','Pear']
#for loop steps through each instance within the stored list. It runs the same code with each iteration. 
#reads as -> for these items; do this thing to each item.

# ':' signifies the start of the loop block. Each compand for the for loop needs to fall within this space. 
for fruit in fruits:
    print(fruit)
    print(fruit+ " Pie")


#excercise 1
#find the average student height WITHOUT using sum or length functions. 

student_heights = [187,190,155,165,181,192,200]
height = 0
students = 0 

for heights in student_heights:
    height += heights
    students += 1

output = round(height/students)

print(output)

#excercise 2
#find the highest score in the class without using the max or min functions

student_scores = [155,175,100,125,200,225]

max_score = 0

for score in student_scores:
    if score > max_score:
      max_score = score
    else:
      pass

print(f"The highest score in the class is: {max_score}")

#excercise 3
#calculate the sum of all even numbers between 1 and 100

even_sum = 0
#for the numbers in the range of 1-100 (not inclusive)
for numbers in range(0,101):
    #if numbers are even.
    if numbers % 2 == 0:
        #add numbers to the end sum
        even_sum += numbers
    else: 
        #otherwise skip.
        pass

print(even_sum)

#excercise 4 - Fizz Buzz
#print all numbers 1-100. If divisible by 3 > fizz, if divisible by 5 > buzz. if divisible by 3 and 5 > fizz buzz

for number in range(0,101):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')

    elif number %3 == 0:
        print('Fizz')
    
    elif number%5 == 0:
        print('Buzz')

    else:
        print(number)

