# SINGLE INHERITANCE

# What is single inheritance?
# Single inheritance is a type of inheritance where a child class inherits the
# properties and methods of a single parent class

# EXAMPLE :

class Father:
    def guide (self):
        print("This is the guide method of parent class")

class Children(Father):
    def play(self):
        print("This is the play method of child class")

c1 = Children()
c1.play()
c1.guide()


# Parent class
class Vehicle:
    def start(self):
        return "Vehicle started"

# Child class inheriting from Vehicle
class Car(Vehicle):
    def drive(self):
        return "Car is driving"


my_car = Car()

print(my_car.start())  
print(my_car.drive())
