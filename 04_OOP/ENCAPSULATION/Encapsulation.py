# ENCAPSULATION IN OOP
# Encapsulation is the concept of bundling data and methods that operate on that data within a single
# unit, called a class or object. This helps to hide the implementation details of an object from
# the outside world and provides a way to control access to an object's data.
# Encapsulation is achieved by using access modifiers such as public, private, and protected.


# PROTECTED MEMBERS
# Protected members are members that are accessible within the same class and its subclasses.
# In Python, we can use a single underscore prefix to create protected members.

# EXAMPLE 
class Employee:
    def __init__(self, name, salary):
        self._name = name  # protected member
        self._salary = salary  # protected member
       
    def admin(self):
        print(self._name,self._salary)  # protected member

c1 = Employee("khurran",150000)
c1.admin()
print(c1._name) # like ths you can access protected members but u wont have to 

# PRIVATE VARIABLE ABD PRIVATE MEMBERS
# PRIVATE VARIABLE ARE the attributes of class the variables that are not accessible from outside the class

# private members are the actions os methods od class that are not accessible from outside the class
# to write we use double underscore prefix

# EXAMPLE:

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def __id(self):
        print(122222)

    def admin(self):
        print(self.__name,self.__salary,self.__id)

c2 = Employee("ali",10000)
c2.admin()  # this will print khurran 150000
# c2.__name() this will cause an error 

# NAME MANGLING 
# WITH NAME MANGLING WE CAN ACCESS THE PRIVATE MEMBERS AND VARIABLES FROM OUTSIDE THE CLASS

# EXAMPLE:

class MyClass:
    def __init__(self, name):
        self.__name = name  # Private attribute with name mangling

    def get_name(self):
        return self.__name  # Method to access the private attribute

# Creating an instance of MyClass
obj = MyClass("John")

# Accessing the private attribute through the public method
print(obj.get_name())  # Output: John

# Trying to access the private attribute directly (This will raise an AttributeError)
# print(obj.__name)    # Uncommenting this line will raise an error

# Accessing the mangled attribute directly by using its mangled name
print(obj._MyClass__name)  # Output: John

