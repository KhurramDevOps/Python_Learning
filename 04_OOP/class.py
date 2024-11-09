# OOP STANDS FOR (OBJECT ORIENTED PROGRAMMING).
# IT IS A PROGRAMMING PARADIGM BASED ON THE CONCEPT OF "OBJECTS
# THAT HAVE PROPERTIES AND METHODS COMBINING TO PRODUCE AN INHERENT
# BEHAVIOR IN SOFTWARE USING OBJECTS, WHICH CAN contain data, in the
# form of fields, and code, in the form of methods."
# 
# CLASS IS A BLUEPRINT FOR CREATING OBJECTS. IT CONTAINS PROPERTIES
# AND METHODS THAT DEFINE THE BEHAVIOR OF AN OBJECT.

# IN SIMPLE CLASS IS THE BLUE PRINT OF A OBJECT 
# FOR EXAMPLE:
# HOUSE PRINT IS A CLASS AND HOUSE IS A OBJECT

# CLASS HAVE ATTRIBUTES AND ACTIONS
# ATTRIBUTES ARE THE PROPERTIES OF CLASS
# ACTIONS ARE THE METHODS OF CLASS

# OBJECT S ARE INSTANCES OF CLASS
# FOR EXAMPLE:
# HOUSE IS A OBJECT AND HOUSE PRINT IS A CLASS
# HOUSE IS AN INSTANCE OF HOUSE PRINT CLASS


# EXAMPLE OF CLASS AND OBJECT

class Dog:
    # CLASS ATTRIBUTES 
    # Attributes is used for recognition
    # without self parameter attributes are called static attributes
    breed = "German"
    color = "black" # static attribute
    age = 3 
    # CLASS ACTIONS
    def bark(self):
        print("Woof woof")
    def eat(self):
        print("Dog is eating")

D1 = Dog()

print(D1.breed)
print(D1.color)
print(D1.age)

D1.bark()

D1.eat()


class Human():
    name = "khurram"
    age = "18"

    def eat(self):
        print("human is eating")
    def sleep(self):
        print("human is sleeping")

h1 = Human()

print(h1.name)
print(h1.age)

h1.eat()

h1.sleep()


