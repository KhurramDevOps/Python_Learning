# IDENTITY OPERATORS 

# Identity Operators
# Identity operators are used to check if two variables are the same object or not.
# They are used to check the identity of an object.

# There are two identity operators:

# is: Evaluates to True if both variables point to the same object.
# is not: Evaluates to True if both variables point to different objects..


a = [1, 2, 3]
b = a  
c = [1, 2, 3]  

print(a is b)      
print(a is c)      

x = "hello"
y = "hello"
z = "world"

print(x is not y)  
print(x is not z)  
