# TUPLE
# WHAT IS TUPLE
# A tuple is a collection of items which are ordered and immutable.
# TUPLE IS IMMUTABLE

# EXAMPLE :

tu = (1,2,3,4,5,6,7,8,9)
print(tu)
print(type(tu))

# SLICING AND INDEXING IN TUPLE

print(tu[0])
print(tu[1])
print(tu[2])
print(tu[1:3])

tuple1 = (1,3,4,5,6)
tuple2 = (7,8,9,10,11)
print(tuple1 + tuple2)
print(tuple1 * 3)

# if u want to give one value in tuple  then u have to use comma after value
tu = (1,)
print(tu)

# nested tuple
t1 = (1,2,(3,4,(5,6)))
print(tu)

t3 = (tuple1,tuple2)


# TASK 

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




