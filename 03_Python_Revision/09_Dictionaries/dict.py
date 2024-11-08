# DICTIONARY 
# WHAT IS DICTIONARY?
# A dictionary is a collection of key-value pairs. It is an unordered collection of items that can
# be of any data type, including strings, integers, floats, and other dictionaries.
# Each key is unique and maps to a specific value.
# Dictionaries are mutable, meaning they can be changed after creation.
# Dictionaries are denoted by curly brackets {}.

# Example:
person = {"name": "John", "age": 30, "city": "New jersey"}
print(person)  

# Indexing 
print(person["name"])

# different data types in  dictionary
my_dict = {"a" : [1,2,3,4], "b" : [1,2,3,4 ], "c" : (5,4,6)}
print(my_dict["a"])
print(my_dict["b"])
print(my_dict["b"][1])

# taking input
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello {name} you are {age} years old")

# taking input and storing in dictionary
person = {"name": input("Enter your name: "), "age": input("Enter your age:")}
print(person)

# Nested  dictionary
person = {"name": "John", "age": 30, "city": "New jersey"}
person["address"] = {"street": "123 main st", "apartment": 4}
print(person)

# key arbitrary argument

def add(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
        print(kwargs)
add(a = 1, b = 2, c = 3)

dic = dict([(1,"a"),(2,"b"),(3,"c")])
print(dic)


for x , y  in person.items():
    print(x,y)

# using list and enumerate making a dictionary 
my_dict =  {}
li = ["a", "b", "c"]
for i, item in enumerate(li):
    my_dict[i] = item

print(my_dict)
