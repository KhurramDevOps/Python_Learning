# Doc string
# """ """  some thing written  in triple quotes in a function is called docstring
# Doc string is as similar to Comment in python 
# but u can Also print a doc string but you cant print a comment

def even_odd(i):
    """THis  is a doc string"""
    if i % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(even_odd(5))

# # u can print a doc string 

print(even_odd.__doc__)  # this will print the doc string

# Task 
def reverse_string():
    user_input = input("Write a string to reverse : ")
    
    reverse = user_input[::-1]
    return(reverse)
   
    
print(reverse_string())

# Task 
def count_vowels():
    user_input = input("WRite something to count vowels  : ")
    count = 0
    vowels = ["a","e","i","o","u"]
    for i in user_input.lower():
        if i in vowels:
            count += 1
    return count
     
print(count_vowels())  

