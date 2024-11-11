# POLYMORPHISM 
# what is polymorphism?
# it is the ability of an object to take on multiple forms
# it is a key feature of object-oriented programming
# it allows objects of different classes to be treated as objects of a common superclass
# it is achieved through method overriding or method overloading

# method overriding: when a subclass provides a different implementation of a method that is already defined in its
# superclass

# Example:

class Animal:
    def sound(self):
        print("The animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("The dog barks")

class Cat(Animal):
    def sound(self):
        print("the cat meow")

a1 = Animal()
a2 = Dog()
a3 = Cat()

a1.sound()
a2.sound()
a3.sound()

# method overloading: when multiple methods with the same name can be defined, but with different parameters

# EXAMPLE 

class Addition(object):
    def add(self, a, b):
        return a + b
    def add(self, a, b, c):
        return a + b + c
    def add(self, a, b, c, d):
        return a + b + c + d
    
a1 = Addition()
# print(a1.add(2,3)) # it will give error because the same add function so it overload and only the last add function is now exist 
print(a1.add(2,3,4,5)) 

# if you want that either how many argument the add function will take it will give the sum of all the argument then you can use *args in python

class Addition(object):
    def add(self, *args):
        return sum(args)

a2 = Addition()
print(a2.add(2,3,4,5.66,88))


# polymorphism is useful for writing generic code that can work with objects of different classes
# it is also useful for writing code that can work with different types of data
