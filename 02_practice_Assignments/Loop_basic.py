# Assignment 1

for i in range(1,101):
    
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Assignment 2

user_input =  input("Enter the number which table u want : ")
for i in range(1,11):
    print(f" {user_input}  x {i} = {int(user_input) *  (i)}")  

# Assignment 3

for i in range(0,4):
    print("*****")