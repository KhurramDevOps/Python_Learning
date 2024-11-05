# CONTINUE STATEMENT 

# EXAMPLE  
# Write a program that prints the numbers from 1 to 10, but skips the number

for x in range(1,10):
    if x == 2:
        continue
    print(x)

for i in range(1,20):
    if i == 10:
        continue
    print(i)


count = 0
while (count < 3):
    print("bye")
    count = count + 1
    if count == 2:
       continue



#  BREAK STATEMENT

# EXAMPLE
# Write a program that prints the numbers from 1 to 10, but stops at 5

for i in range(1,10):
    if i == 5:
        break
    print(i)

for i in range(1,5):
    if i == 3:
        break
    print("khurram")

count = 0
while (count < 3):
    print("bye")
    break


while True:
    user_input = input("Write your name : ")
    if user_input == "exit":
        break
    print("Type exit to close : ")