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

try:
    # Code that might raise an exception
    num = int(input("Enter a number: "))
    print("You entered:", num)

except ValueError:
    # Code that runs if there's a ValueError (e.g., if input is not a valid integer)
    print("That's not a valid number!")

# DIVISION USING TRY EXCEPT 
try:
    a = int(input("Enter the numerator: "))
    b = int(input("Enter the denominator: "))
    result = a / b
    print("Result:", result)

except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")



# Finally block 
# The finally block in Python is used with try and except to execute code that should
#  run regardless of whether an exception was raised or not.

# example 


try:
   
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)

except ValueError:
   
    print("That's not a valid number!")

except ZeroDivisionError:
    
    print("You can't divide by zero!")

finally:
    # Code in finally block will always execute
    print("End of program.")


# example 2 using file handling

try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)

except FileNotFoundError:
    print("File not found.")

finally:
    file.close()  # Ensures the file is closed, even if an exception occurs
    print("File is closed.")


# Else and finally block
# The combination of else and finally can be useful for writing cleaner code, separating logic that should only happen if everything is
#  successful (in else) from code that must always run for cleanup (in finally).

# Example :

try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Invalid input! Please enter an integer.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
else:
    # This will run only if no exception occurred
    print("The result is:", result)
finally:
    # This will always run
    print("End of program.")




