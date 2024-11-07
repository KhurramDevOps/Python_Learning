# FUNCTION 
# WHAT IS FUNCTION?
# A block of code which can be called multiple times from our program is called a function.
# It takes some inputs, does some operations and gives some output.

# Syntax 
def even_odd(i):

    if i % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

# u can use above function anywhere
user_input = int(input("Enter a Number : "))
even_odd(user_input)


# Types_Of Functions
# 1. Built-in Functions
# 2. User-defined Functions

# BUILT IN FUNCTION:
# A function which is already defined in python is called a built-in function.
# We can use it directly in our program.
# Example: print(), len(), max(), min(), etc.

# EXAMPLE 
li = [1,2,3,4]
print(sum(li))

# USER_DEFINED FUNCTIONS:
# A function which is defined by us is called a user-defined function.
# We can use it in our program after defining it.

# EXAMPLE 

def even_odd(i):

    if i % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

def fun():
    print("Welcome to GFG")

fun()

def add(x,y):
    print(x + y)
add(2,3)

# you can call a function by writing their name with parenthesis

# return 
# return is used to return a value from a function.

# example 
def add(x,y):
    return x + y
print(add(2,3))