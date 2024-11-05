# WHILE LOOP
# A while loop is used to execute a block of code as long as a certain condition is met
# The condition is checked before each iteration of the loop
# The loop will continue to run as long as the condition is true
# Once the condition is false, the loop will stop

#   Example of a while loop

count = 0
while (count < 3):
    print("hello")
    count += 1

condition = True
while (condition):
    user_input = input("Write your name : ")
    if user_input == "exit":
        condition = False
    print("Type exit to close : ")