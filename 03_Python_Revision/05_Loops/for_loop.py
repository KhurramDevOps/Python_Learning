#  FOR LOOPS 
#  ===========
#  A for loop is used to iterate over a sequence (such as a list, tuple,
#  dictionary, set, or string) or other iterable object, executing a block of
#  code for each item in the sequence.
#
#  The general SYNTAX of a for loop is:
#
# for variable in iterable:
    # code to be executed 

# EXAMPLE :

name = "Khurram"

for x in name:
    print(x)

fruits = ["apple","banana","cherry"]

for i in fruits:
    print(i)


things = ("bed","chair","table")
for i in things:
    print(i)

# my_dict =  {"name":"Khurram","age":18}
# for names, age in my_dict:
#     print(f"{names} : {age}")

# USING RANGE
name1 = "khurram"
for x in range(1,5):
    print(name1)

s = "geeks"
for i in s:
    print(i)
 
# Task
for i in range(1,101):
    
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


