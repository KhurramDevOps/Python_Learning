print("--> MINI CALCULATER <--")
# *----------DEFINE FUNCTIONS FOR OPERATIONS----------*
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "ERROR! DIVISION BY ZERO"
# *-----------USING VARIABLES FOR OPERATIONS----------*
x= 19
y= 13
#  *----------PERFORM CALCULATIONS---------*
additon_result = add(x, y)
subtraction_result = subtract(x, y)
multiplication_result = multiply(x, y)
division_result = divide(x, y)
# *---------PRINT RESULTS---------*
print(f"Addition: {x} + {y} = {additon_result}")
print(f"Subtraction: {x} _{y} = {subtraction_result}")
print(f"Multiplication: {x} * {y} = {multiplication_result}")
print(f"Division: {x} / {y} = {division_result}")


