# OOP REVISION 
# OOP STANDS FOR OBJECT ORIENTED PROGRAMMING
# IT IS A PROGRAMMING PARADIGM BASED ON THE CONCEPT OF "OBJECTS
# ANYTHING THAT CAN BE REPRESENTED AS AN OBJECT CAN BE MANIPULATED USING OOP
# OOP IS USED TO SIMPLIFY THE COMPLEXITY OF PROGRAMMING BY BREAKING DOWN

# CLASS AND OBJECTS
# CLASS IS A BLUEPRINT OR A TEMPLATE THAT DEFINES THE PROPERTIES AND BEHAVIOUR
# OF AN OBJECT

class Dog:
    def __init__(self,name,breed,age):
        self.name = name
        self.breed = breed
        self.age = age

    def sound(self):
        print("Woof")
    def eat(self,meal):
        print(f"{self.name} is eating {meal}")

d1 = Dog("bella","germen","4")

print(d1.name)
print(d1.breed)
print(d1.age)

d1.sound()
d1.eat("Biscuit")

print()

d2 = Dog("max","bulldog","5")
print(d2.name)
print(d2.breed)
print(d2.age)
d2.sound()
d2.eat("meat")


# INHERITANCE
# IT IS A MECHANISM THAT ALLOWS ONE CLASS TO INHERIT THE PROPERTIES
# AND BEHAVIOR OF ANOTHER CLASS

class Father:
    def guide(self):
        print("I will guide you")
    def work(self):
        print("I will work")
class Child(Father):
    def play(self):
        print("I will play")

    def eat(self):
        print(" I am eating")

c1 = Child()
c1.play()
c1.eat()
c1.guide()
c1.work()

# MUltiple Inheritance
class Father:
    def show_father_traits(self):
        return "Father's traits"

class Mother:
    def show_mother_traits(self):
        return "Mother's traits"

class Child(Father, Mother):
    def show_child_traits(self):
        return "Child's traits"

# Testing
child = Child()
print(child.show_father_traits())  # Output: Father's traits
print(child.show_mother_traits())  # Output: Mother's traits
print(child.show_child_traits())   # Output: Child's traits

# Multilevel Inheritance
class Grandfather:
    def show_grandfather_traits(self):
        return "Grandfather's traits"

class Father(Grandfather):
    def show_father_traits(self):
        return "Father's traits"

class Child(Father):
    def show_child_traits(self):
        return "Child's traits"

# Testing
child = Child()
print(child.show_grandfather_traits())  # Output: Grandfather's traits
print(child.show_father_traits())       # Output: Father's traits
print(child.show_child_traits())        # Output: Child's traits


# Hierarchical Inheritance
class Grandfather:
    def show_grandfather_traits(self):
        return "Grandfather's traits"

class Father(Grandfather):
    def show_father_traits(self):
        return "Father's traits"

class Mother(Grandfather):
    def show_mother_traits(self):
        return "Mother's traits"

# Testing
father = Father()
mother = Mother()
print(father.show_grandfather_traits()) # Output: Grandfather's traits
print(father.show_father_traits())      # Output: Father's traits
print(mother.show_grandfather_traits()) # Output: Grandfather's traits
print(mother.show_mother_traits())      # Output: Mother's traits

# HyBRID INHERITANCE

class Grandfather:
    def show_grandfather_traits(self):
        return "Grandfather's traits"

class Father(Grandfather):
    def show_father_traits(self):
        return "Father's traits"

class Mother:
    def show_mother_traits(self):
        return "Mother's traits"

class Child(Father, Mother):
    def show_child_traits(self):
        return "Child's traits"

# Testing
child = Child()
print(child.show_grandfather_traits())  # Output: Grandfather's traits
print(child.show_father_traits())       # Output: Father's traits
print(child.show_mother_traits())       # Output: Mother's traits
print(child.show_child_traits())        # Output: Child's traits


# ENCAPSULATION:

class Dog:
    def __init__(self,name,breed,age):
        self.__name = name
        self.__breed = breed
        self.__age = age

    def __sound(self):
        print("Woof")
    def __eat(self,meal):
        print(f"{self.__name} is eating {meal}")

c1 = Dog("Bella","germen","4")
c1.__name = "Bella"  # This will raise an AttributeError
# c1.__sound()  # This will raise an AttributeError
# c1.__eat("Biscuit")  # This will raise an AttributeError

#how to access the private attributes
c1._Dog__name = "Bella"
c1._Dog__sound()
c1._Dog__eat("Biscuit")
print(c1._Dog__name)
print(c1._Dog__breed)
print(c1._Dog__age)  # This will print 0 because we didn't pass


# POLYMORPHISM
class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Woof"
class Cat(Animal):
        def sound(self):
            return "Meow"
      
      
c2 = Cat()
c3 = Dog()
print(c2.sound())  # Output: Meow
print(c3.sound())  # Output: Woof

#ABSTRACTION
from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    class Circle:
        def __init__(self,r):
            self.radius = r
        def area(self):
            return 3.14 * (self.radius ** 2)
        def perimeter(self):
            return 2 * 3.14 * self.radius
    class Rectangle:
        def __init__(self,l,w):
            self.length = l
            self.width = w
        def area(self):
            return self.length * self.width
        def perimeter(self):
            return 2 * (self.length + self.width)
                
    c = Circle(5)
    r = Rectangle(4,5)
    print(c.area())  
    print(c.perimeter())  
    print(r.area())  
    print(r.perimeter())  
                