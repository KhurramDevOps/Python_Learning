# ABSTRACTION

# What is abstraction ?
# Abstraction is the process of hiding the implementation details of an object from the user and showing only the necessary information
# Abstraction is a fundamental concept in object-oriented programming (OOP) that helps to reduce complexity
# Abstraction helps to improve the modularity of the code and makes it easier to maintain and extend
# Abstraction is achieved through encapsulation, inheritance, and polymorphism

# EXAMPLE :
# A car is an example of abstraction. A car has many features like engine, wheels, steering
# But when we drive a car, we don't need to know how the engine works or how
# the wheels rotate. We just need to know how to drive the car. 
# This is an example
# of abstraction where we are hiding the implementation details of the car and showing

from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    @abstractmethod
    def printDetails(self):
        pass

    def accelerate(self):
        print("Accelerating...")

    def break_applied(self):
        print("Car stopped")

    
class Hatchback(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def sunroof(self):
        print("Not having the feature of sunroof")

class Suv(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
    
    def sunroof(self):
        print("Having the feature of sunroof")

car1 = Hatchback("maruti","suzuki","2022")

car1.printDetails()
car1.accelerate()
car1.break_applied()


