#hello world print function
print('hello world')
#prints output contained within the function can pass strings, variables,function outputs, etc. 
#strings must be passed with complete quotes or within a variable.


#\n can be utilized in string to have string components printed on a different line in terminal. 
print('hello world\nhello world \nhello world')

#string concatenation can be used in different ways to create the same result. 
print('hello ' + 'angela')
print('hello'+' '+'angela')
print('hello'+' angela')

#we can use the input function to create a variable in response to an answer. str function ensures it's considered as a string first. 

name = str(input("What's your name? "))
print(name)

#can also use this to find the number of characters within a string

name_len =  str(input("What's your name? "))
print(len(name))