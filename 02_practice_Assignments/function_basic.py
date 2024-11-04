# ASSIGNMENT 1 
def count_vowels():
    user_input = input("WRite something to count vowels  : ")
    count = 0
    vowels = ["a","e","i","o","u"]
    for i in user_input.lower():
        if user_input in vowels:
            count += 1
    return count
     
print(count_vowels()) 


# ASSIGNMENT 2
def reverse_string():
    user_input = input("Write a string to reverse : ")
    
    reverse = user_input[::-1]
    return(reverse)
   
    
print(reverse_string())