# INHERITANCE IN OOP

# Inheritance is a mechanism in object-oriented programming (OOP) that allows one class to inherit
# the properties and behavior of another class. The class that is being inherited from is called the
# parent class or the superclass, and the class that is doing the inheriting is called the child
# class or the subclass.

# Inheritance is useful for code reuse and for creating a hierarchy of related classes.

# It allows a child class to inherit the attributes and methods of a parent class and to add new
# attributes and methods or override the ones inherited from the parent class.

# EXAMPLE OF INHERITANCE IN OOP

# Parent class
class Animal:
    def speak(self):
        return "Animal sound"

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        return "Woof!"

# Creating an instance of Dog
dog = Dog()

# Accessing methods from both the parent and child classes
print(dog.speak())  
print(dog.bark())   

# Parent class
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start_engine(self):
        return "Engine started"

# Child class adding new attributes and methods
class Car(Vehicle):
    def __init__(self, brand, year, model):
        self.brand = brand
        self.year = year 
        self.model = model

    def honk(self):
        return "Beep beep!"

# Creating an instance of Car
my_car = Car("Toyota", 2020, "Corolla")

# Accessing attributes and methods
print(my_car.brand)          
print(my_car.year)           
print(my_car.model)          
print(my_car.start_engine()) 
print(my_car.honk())         

