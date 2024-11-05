# ASSIGNMENT 

# Task 
# way 1
li = [1,3,23,45,7,9]
user_choice = int(input("Enter rank of  highest number u want to see : "))
if user_choice == 1:
    print(max(li))  
elif user_choice == 2:
    print(li[2])
elif user_choice == 3:
    print(li[-1])
elif user_choice == 4:
    print(li[-2])
elif user_choice == 5:
    print(li[1])
elif user_choice == 6:
    print(min(li))
else:
    print("Invalid choice")

# way 2 
li = [1,3,23,45,7,9]
user_input = int(input("Enter rank of highest number you wanna see : "))
sorted_list = li.sort(reverse=True)
print(li[user_input-1])