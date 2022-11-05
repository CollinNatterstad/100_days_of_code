#class inheritance

#allows methods to be transfered downstream to other classes where there is overlap. Reducing redundancy in the code. 
#you can inherit attributes and methods. 

#passing the Animal class into the Fish class allows us to gain access to all of it's functionality with the super() method/
#class Fish(Animal):

    #def __init__(self):
        #refers to all of the methods/attributes contained within the super (or above) class. 
        #super().__init__()

#example from video
class Animal:
    def __init__(self):
        self.num_eyes = 2


    def breathe(self):
        print("inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

#we can even change the super'd function within the second class. 
#when this condition is called it can then be modified to perform specific tasks within this class.
#this is great when you need to make alterations but don't want to change the method itself. 
    def breath(self):
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("moving in water")


#with run we can demonstrate that Fish has gained access to the attributes and methods within the animal class.
fish = Fish()
print(fish.num_eyes)
fish.breath()
fish.swim()
