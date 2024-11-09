# CONSTRUCTOR IN OOP
# A constructor is a special method in a class that is automatically called when an object is created from
# that class. It is used to initialize the attributes of the class.

# The constructor is defined with the __init__ method.
# The __init__ method is a special method in Python classes. It is automatically called when an
# object of that class is created.
# The __init__ method is used to initialize the attributes of the class.
# The __init__ method does not return any value.

# what is self parameter?
# self is a reference to the current instance of the class and is used to access variables and methods
# from the class.
# It is not a keyword and is used as a convention.
# It is not necessary to use self to access variables and methods from the class, but it is
# a good practice to use it.

# EXAMPLE 

class Dog:
    def __init__(self, breed, age): #with self attribute is called instance attribute 
        self.breed = breed
        self.age = age
        
    def bark(self):
        print("Woof!")
    def eat(self,meal):
        print("The dog is eating ",meal)
d1 = Dog("german",18)

print(d1.breed)
print(d1.age)

d1.bark()
d1.eat("chicken")  

d2 = Dog("russian",5)

print(d2.breed)
print(d2.age)

d2.bark()
d2.eat("beef")




