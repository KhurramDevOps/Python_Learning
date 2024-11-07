# LIST
#  WHAT IS LIST 
#  LIST IS A COLLECTION OF ITEMS WHICH ARE ORDERED AND CHANGEABLE
#  LIST IS DEFINED BY THE SQUARE BRACKETS []

li = [ 1, 2, 3, 4, 5]
print(li)

# len()
# to find the length of the list
print(len(li))

# SLICING IN LIST 
# With slicing our original list never change it gives us another sliced list
my_list = [1,2,3,4,5,"khurram",5.5,True]
print(my_list[0])
print(my_list[1:7])
print(my_list[1:])
print(my_list[:7])
print(my_list[1:8:2])

# negative slicing indexing:
# -1 is the last element
print(my_list[-1])
print(my_list[-5:-1])
print(my_list[-5:])

# NESTED LIST
# A list can contain another list
my_list = [1,2,3,[4,5,6]]
print(my_list[3])

# example 
li2 = []
for i in range(1,5):
    user_input = int(input(f"enter {i} number : "))
    li2.append(i)
print(li2)

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


