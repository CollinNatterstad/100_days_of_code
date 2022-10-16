#creating a class

#class is similar to a function an needs to be constructed. 

#does not require () like a function/method does.
#does utilize PascalCase < example of pascal case. 
class User:

    #functions that exist within a class are functions specific to that class. 
    #init function creates the initial starting value 
    #initialized every time the class is called. the parameters within the () are the values that we pass in with initialization. New instance MUST provide this data. 
    #very useful for when you're creating a loads of the same kinds of objects with different values. 
    def __init__(self,user_id,user_name):
        #these are attributes of the user class. They can be accessed once initialized. 
        #these set the value of self.name equal to the passed in parameter.
        self.id = user_id 
        self.name = user_name
        #we can set a value equal to a class just like a normal variable. 
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1 
        self.following += 1

user1 = User(user_id='1' , user_name = 'John')
user2 = User(user_id='2', user_name='amy')

user2.follow(user1)

print(user1.following)
print(user1.followers)
print(user2.followers)
print(user2.following)
