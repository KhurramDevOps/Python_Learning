# ASSIGNMENT 

# TASK :

tu= ()
for i in range(1,4):
    user_input = input("Enter age press enter , enter name press enter , enter student id  press enter: ")
    tu += (user_input,)
    
print(tu) 
my_list = list(tu)
del my_list[1]
my_list.insert(1,"khurram")
my_tuple = tuple(my_list)
print(my_tuple)