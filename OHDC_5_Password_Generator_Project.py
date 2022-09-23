import random 
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

print("Welcome to your password generator")
num_upper = int(input("How many upper case letters would you like?\n"))
num_lower = int(input("How many lower case letters would you like?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password_characters = []

# selecting upper case
for number in range(1,(num_upper+1)):
    password_characters.append(random.choice(upper))
#selecting lower case
for number in range(1,num_lower+1):
    password_characters.append(random.choice(lower))
#selecting 
for number in range(1,num_symbols+1):
    password_characters.append(random.choice(symbols))

for number in range(1,num_numbers+1):
    password_characters.append(random.choice(numbers)) 

password = ''

for item in password_characters:
    password += random.choice(item)
    
print(password)
print(len(password))