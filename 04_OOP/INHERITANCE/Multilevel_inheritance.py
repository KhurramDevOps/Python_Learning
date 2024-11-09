# MULTILEVEL INHERITANCE

# What is Multilevel inheritance?
# Multilevel inheritance is a type of inheritance where a child class inherits properties and methods from a parent
# class and the parent class also inherits properties and methods from another parent class.

# Example of Multilevel Inheritance


class GrandFather:
    def guide (self):
        print("\nThis is the guide method of grand parent class")

class Father(GrandFather):
    def teach(self):
        print("This is the teach method of parent class")
    def work(self):
        print("This is the work method of parent class")

class Children(Father):
    def play(self):
        print("This is the play method of child class")

f1 = Father()
f1.guide()
f1.work()
f1.teach()


c1 = Children()
c1.guide()
c1.teach()
c1.work()
c1.play()