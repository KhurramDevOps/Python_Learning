#  Ask the user to enter the name 
num_list = []
user_name =  input("Please enter your name: ")
print ()

#  Ask the user for three favorite number and collect them in a list
for x in range(1,  4):
    user_number : int = int(input(f"Please enter your {x} favorite number : "))
    num_list.append(user_number)
    print(num_list)


# check the favorite number is even or odd
print(f"\nHello, {user_name}! Let's explore your favorite numbers:\n ") 
for num in num_list:
    if num % 2 == 0:
        print(f"The number {num} is even")
    else :
        print(f"The number {num} is odd")
    
# Display each number and its square 
print()
for num in num_list:
    print(f"The number {num} and its square is : ({num}, {num ** 2})")

# Sum of favorite number 
sum_of_number = sum(num_list)
print(f"\nWonderful! The sum of your favorite numbers is : {sum_of_number}")

# Determine the sum of numbers is a Prime  number or not 
Is_prime =  True
if sum_of_number <= 1:
    Is_prime = False
for i in range(2,sum_of_number):
    if sum_of_number % i == 0:
        Is_prime = False

if Is_prime:
    print(f"Wow! The number  {sum_of_number} is a prime number")
else:
    print(f"Sorry, the number {sum_of_number} is not a prime number")