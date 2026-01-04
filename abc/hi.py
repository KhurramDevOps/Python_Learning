# Q6) Write a recursive function count_occ(lst, target, index) that returns how many times target appears in
# the list.

def count_occ(lst, target, index=0):
    # Base case: if index reaches the length of the list, return 0
    if index == len(lst):
        return 0
    
    elif lst[index] == target:
        # If it matches, count it and recurse for the next index
        return 1 + count_occ(lst, target, index + 1)
    else:
        # If it doesn't match, just recurse for the next index
        return count_occ(lst, target, index + 1)
# Example usage:
my_list = [1, 2, 3, 2, 4, 2, 5]
target_value = 2
print(count_occ(my_list, target_value))  # Output: 3


# Q7) Write a function make_multiplier(n) that returns another function which multiplies numbers by n.
# Example:
# double = make_multiplier(2)
# print(double(5)) # Output: 10

def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

# Example usage:

double = make_multiplier(2)
print(double(5))  # Output: 10

# Q8) Write a function fibonacci(n) that returns the nth Fibonacci number using recursion.

def fibonacci(n):
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case
        return fibonacci(n - 1) + fibonacci(n - 2)
    
# Example usage:
print(fibonacci(6))  # Output: 8

# Q8) Write a recursive Fibonacci function that counts how many times it has been called. Print the total
# number of recursive calls for input 6.

call_count = 0
def fibonacci_with_count(n):
    global call_count
    call_count += 1
    
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case
        return fibonacci_with_count(n - 1) + fibonacci_with_count(n - 2)
    
# Example usage:
call_count = 0  # Reset call count
fibonacci_with_count(6)
print(call_count)  # Output: Total number of recursive calls for input 6


# Q9) Create a function: def profile(name, age=18, country="Pakistan"):
# Call it using all combinations:
# • Only name
# • Name + age
# • Name + country (keyword)
# • All arguments

def profile(name, age=18, country="Pakistan"):
    return f"Name: {name}, Age: {age}, Country: {country}"

# Example usages:
print(profile("Alice"))  # Only name
print(profile("Bob", 25))  # Name + age
print(profile("Charlie", country="USA"))  # Name + country (keyword)
print(profile("David",  country="Canada", age=30))  # All arguments


# Q10) Write a recursive function print_reverse(lst, index) that prints the list in reverse order using recursion
# only and no loops like append each elememnt to another list and then print that list.
# i want the output in new list which is reversed using recursion 
reversed_list = []
def collect_reverse(lst, index=None):
    if index is None:
        index = len(lst) - 1
    
    # Base case: if index is less than 0, return
    if index < 0:
        return
    
    # Append the current element to reversed_list
    reversed_list.append(lst[index])
    
    # Recurse for the previous index
    collect_reverse(lst, index - 1)
collect_reverse([1,2,3,4,5])
print(reversed_list)  # Output: [5, 4, 3, 2, 1]