# ERROR HANDLING 
# WHAT IS ERROR HANDLING IN PYTHON?
# eror handling is a way to handle the errors that occur during the execution of a program.
# it is used to prevent the program from crashing and to provide a meaningful error message to the user
# there are two types of error handling in python:
# 1. try-except block
# 2. try-except-finally block
# 3. try-except-else block
# 4. try-except-else-finally block

# Example 
try:
    x = 5 / 0
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")


