# HYBRID INHERITANCE 

# WHAT IS HYBRID INHERITANCE?
# HYBRID INHERITANCE IS A COMBINATION OF MULTIPLE INHERITANCE
# AND MULTIPLE INHERITANCE IS A COMBINATION OF MULTIPLE PARENT CLASSES
# AND MULTIPLE INHERITANCE IS USED WHEN WE WANT TO INHERIT PROPERTIES
# AND BEHAVIOR FROM MULTIPLE CLASSES.

# Example of Hybrid Inheritance :

class Parent1:
    def guide(self):
        print("\nThis is the guide method of parent1 class")
    def work(self):
        print("This is the work method of parent1 class")
class Parent2:
        def guide(self):
            print("This is the guide method of parent2 class")
        def work(self):
            print("This is the work method of parent2 class")
class Parent3(Parent1,Parent2):
        def guide(self):
            print("This is the guide method of parent3 class")
        def work(self):
            print("This is the work method of parent3 class")
class Children(Parent3):
        def play(self):
            print("This is the play method of child class")
        def study(self):
            print("This is the study method of child class")
c = Children()
c.guide()
c.play()
c.study()
c.work()  

# ANother example:

# Base Class 1
class Animal:
    def speak(self):
        return "Animal Sound"

# Base Class 2
class Wild:
    def habitat(self):
        return "Lives in the wild"

# Derived Class using Multiple Inheritance
class Dog(Animal, Wild):
    def sound(self):
        return "Barks"

# Multilevel Inheritance
class GermanShepherd(Dog):
    def breed(self):
        return "German Shepherd"

# Creating an object of GermanShepherd
gs = GermanShepherd()

# Accessing methods from different inheritance structures
print(gs.speak())          # From Animal class (single inheritance path)
print(gs.habitat())        # From Wild class (multiple inheritance path)
print(gs.sound())          # From Dog class (multilevel path)
print(gs.breed())          # Own method in GermanShepherd class
