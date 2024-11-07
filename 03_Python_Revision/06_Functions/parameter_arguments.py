# PARAMETERS AND ARGUMENTS IN A FUNCTION
# A function can take arguments, which are the values that are passed to the function when it is
# called. These arguments are used inside the function to perform some operation.

# PARAMETER:
# A parameter is a variable that is used inside a function to represent the argument that is
# passed to the function when it is called.

# EXAMPLE 
def even_odd(i): # THE i IN PARENTHESIS IS PARAMETER

    if i % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")


# ARGUMENTS:
# An argument is the value that is passed to a function when it is called.
# It is the actual value that is used inside the function.

# EXAMPLE
user_input = int(input("Enter a Number : "))
even_odd(user_input) #HERE user_input in parenthesis is Argument


# TYPES OF ARGUMENTS.
# 1. Default Argument 
 
#  Example:
def greet(name = "User"):
    return("Hello " + name)

print(greet("khurram"))
print(greet())  #if i dont give name argument then it will uses default name 

def add(x=5,y=2):
    print(x + y)
add(2,)
add()

# IMPORTANT NOTE  IF AFTER GIVING DEFAULT ARGUMENTS YOU DONT ENTER ANOTHER PARAMETER TO RIGHT 
# IF U WANT TO ENTER THE ARGUMENT THE ARGUMENT SHOULD BE DEFAULT

# 2. Positional Argument

# EXAMPLE:

def intro(name,age):
    print(f"my name is {name} and my age is  {age}")

intro("khurram" , 20)
# you have to be careful  about the order of arguments
intro(20,"khurram") # this will make the sentence wrong

# 3. Keyword Argument

# EXAMPLE:
def intro(name,age):
    print(f"my name is {name} and my age is  {age}")
    
intro(name="khurram",age=20)
intro(age=20,name="khurram")
# you can use keyword arguments in any order 

# Arbitrary Keyword Argument
# This is used to pass a variable number of keyword arguments to a function.

# Example 
# *args 
# it returns a tuple
def add(*args):
    print(args)
    return sum(args)

print(add(1,2,3,4,5))


# *kwargs
# it returns a dictionary
def greet(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} : {value}")

greet(a = 1, b = 2,  c = 3)