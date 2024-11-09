# MULTIPLE INHERITANCE

# What is Multiple inheritance?
# Multiple inheritance is a feature of object-oriented programming (OOP) that allows a class to inherit
# properties and methods from more than one parent class.

# EXAMPLE:

class Father:
    def guide (self):
        print("\nThis is the guide method of parent class")
class Mother:
    def teach(self):
        print("This is the teach method of parent class")
    def cook(self):
        print("This is the cook method of parent class")
class Children(Father,Mother):
    def play(self):
         print("This is the play method of child class")

c1 = Children()
c1.guide()
c1.teach()
c1.cook()
c1.play()