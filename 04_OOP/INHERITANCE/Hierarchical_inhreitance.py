# Hierarchical Inheritance

# What is Hierarchical Inheritance?
# HIERARCHICAL INHERITANCE IS USED WHEN WE WANT TO INHERIT PROPERTIES
# AND BEHAVIOR FROM ONE CLASS AND THAT CLASS INHERIT FROM MULTIPLE CLASSES
# BUT THE CHILD CLASS IS NOT A CHILD OF ALL THE PARENT CLASSES.

# Example of Hierarchical Inheritance:

class Parent:
    def guide(self):
        print("\nThis is the guide method of parent class")
    def work(self):
        print("This is the work method of parent class")

class Children1(Parent):
    def play(self):
        print("This is the play method of child class")
    def study(self):
        print("This is the study method of child class")

class Children2(Parent):
    def dance(self):
        print("This is the dance method of child class")
    def sing(self):
        print("This is the sing method of child class")

c1 = Children1()
c1.guide()
c1.play()
c1.study()
c1.work()

c2 = Children2()
c2.guide()
c2.dance()
c2.sing()
c2.work()
