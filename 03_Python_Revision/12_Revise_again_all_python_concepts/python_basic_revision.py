# # REVISION ALL PYTHON CONCEPTS AGAIN !

# # Print function
# print("Hello")
# print("Khurram")

# primitive data type 

# # String
# # Anything written inside the quotes is a string
# name = "Khurram"
# print(name)
# print(type(name))

# # Slicing ,indexing and stepping
# msg = "hello hoe are you"
# print(msg[3])

# print(msg[1:5])
# print(msg[::2])
# print(msg[1:12:2])
# print(msg[-1])

# reverse string
# print(msg[::-1])

# String Functions
# msg = "hello hoe are you"
# print(msg.upper())
# print(msg.lower())
# print(msg.capitalize())
# print(msg.title())
# print(msg.count("o"))
# print(msg.find("o"))
# print(msg.replace("o","a"))
# print(msg.split(" "))
# print(msg.strip())
# print(msg.center(50,"*"))
# print(msg.ljust(50,"*"))
# print(msg.rjust(50,"*"))
# print(msg.startswith("h"))
# print(msg.endswith("u"))
# print(msg.isalpha())
# print(msg.isalnum())
# print(msg.islower())
# print(msg.isupper())
# print(msg.isspace())
# print(msg.isdigit())
# print(msg.isnumeric())
# print(msg.isidentifier())
# print(msg.isprintable())
# print(msg.istitle())
# print(msg.islower())
# print(msg.isupper())


# # Types of inverted commas
# # Single quotes
# print('hy')
# print('some one said "hy"')
# # Double quotes
# print("bye")
# print("some one said 'bye'")
# # Triple quotes
# print(""" hello 
# world someone "said" """)

# # integer
# # any number is called integer
# num = 55
# print(type(num))

# # Float
# # any decimal number is called float
# num = 55.55
# print(type(num))

# # Escape sequence
# # \n - new line
# print("hello \n world")
# # \t - tab
# print("muhammad \t khurram")
# # \r - carriage return
# print("hello \r world")
# # \' \'
# print("hello \"said\"") 
# print("hello \\ khurram")

# Variables
# Variables are used to store data
# you can also say it a container 

# name = "Khurram"
# print(name)

# # Rules OF variables
# # 1. variable name nt contain number at start
# 2name = "khurram"
# # 2. variable name nt contain space
# first name = " muhammad"
# # 3 . Variable name nt contain special character
# name$ = "hy"
# # 4 . Variable name not use predefined keyword
# class = "khurram"
# print  = "hy"


# Rule to do 

# variable name should be meaning full
# variable name should be short

# number = 10
# name = "khurram"
# age = 18

# # Input function
# # input() function is used to take input from user

# user_input = int(input("Enter a number : "))
# print("you entered :",user_input)

# IF STATEMENTS
# IF STATEMENT IS USED TO CHECK THE CONDITION

# i = 10
# if i > 10:
#     print("greater")
# elif i < 10:
#     print("smaller")
# else:
#     print("equal")

# # NESTED IF 
# # IF STATEMENT INSIDE IF STATEMENT

# marks = 97
# if marks > 90:
#     print("A grade")
#     if marks > 95:
#         print("A+ grade")
# else:
#     print("b grade")


     
# LOOPS
# FOR LOOP
# FOR LOOP IS USED TO ITERATE OVER A SEQUENCE

# name = "khurram"
# for i in name:
#     print(i,end=" ")

# for i in range(0,11,2):
#     print(i)

# # NESTED LOOP
# for x  in range(1,4):
#     for y in range(1,4):
#         print(x,y)

# # WHILE LOOP
# # WHILE LOOP IS USED TO ITERATE OVER A SEQUENCE
# score  = 0
# while score < 5:
#     print("score is",score)
#     score += 1

# # CONTROL STATEMENTS
# # BREAK STATEMENT
# # BREAK STATEMENT IS USED TO TERMINATE THE LOOP
# for i in range(1,11):
#     print(i)
#     if i == 5:
#         break

# # CONTINUE STATEMENT
# # CONTINUE STATEMENT IS USED TO SKIP THE CURRENT ITERATION
# for i in range(1,11):
#     if i == 5:
#         continue
#     else:
#         print(i)

# FUNCTION
# FUNCTION IS A BLOCK OF CODE THAT CAN BE CALLED SEVERAL TIMES FROM DIFFERENT
# PARTS OF THE PROGRAM

# def even_odd(x):
#     if x % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# def main():
#     user_input = int(input("enter a number : "))
#     print(even_odd(user_input))

# main()

# # DOC STRING IN FUNCTION
# # DOC STRING IS USED TO DOCUMENT THE FUNCTION
# def even_odd(x):
#     """
#     This function checks whether the number is even or odd
#     Parameters:
#     x (int): The number to be checked
#     Returns:
#     str: "even" if the number is even, "odd" if the number is odd
#     """
#     if x % 2 == 0:
#         return "even"
#     else:
#         return "odd"

# print(even_odd(int(input("enter a number"))))

# # you can print the doc string of the function
# print(even_odd.__doc__)


# NON PRIMITIVE DATA TYPES
# LIST
# LIST IS A COLLECTION OF ITEMS WHICH CAN BE OF ANY DATA TYPE INCLUDING STRINGS, INTE
# GERS, FLOATS, AND OTHER LISTS

# li = [1,2,3,4,5,"khurram",5.5,True]
# print(li)

# li = ["k","h","u","r","r","a","m"]
# my_str = ''.join(li)
# print(my_str)


# # INdexing , SLicing and Stepping
# print(li[0])
# print(li[-1])
# print(li[1:3])
# print(li[1:])
# print(li[:3])
# print(li[1:5:2])
# print(li[::2])
# print(li[::-1])

# # LIST FUNCTIONS
# li = [1,2,3,4,5,"khurram",5.5,True]
# li2 = [1,2,5,8,3,4,5]
# print(len(li))
# print(li.count(5))
# print(li.index(5))
# li.append(6)
# print(li)
# li.insert(2,7)
# print(li)
# li.remove(5)
# print(li)
# li.pop(2)
# print(li)
# li2.sort()
# print(li2)
# li2.reverse()
# print(li2)
# li.clear()
# print(li)
# li.extend([1,2,3])
# print(li)
# li.copy()
# print(li)
# index = li.index(2)
# print(index)


# TUPLE 
# TUPLE IS A COLLECTION OF ITEMS WHICH CAN BE OF ANY DATA TYPE INCLUDING STRINGS, 
# INTEGERS, FLOATS, AND OTHER TUPLES

# tu = (1,2,3,4,5,"string")
# print(tu)

# # indxing , slicing , stepping
# print(tu[0])
# print(tu[-1])
# print(tu[1:3])
# print(tu[1:])
# print(tu[:3])
# print(tu[1:5:2])
# print(tu[::2])
# print(tu[::-1])

# # Tuple functions
# tu = (1,2,3,4,5,"string")

# print(len(tu))
# print(tu.count(1))
# print(tu.index(1))


# DICTIONARY
# DICTIONARY IS A COLLECTION OF KEY VALUE PAIRS
# DICTIONARY IS MUTABLE
# DICTIONARY IS INDEXED BY KEY

# dict = {"name":"John","age":30,"city":"New York"}
# print(dict)

# print(dict["name"])
# print(dict["age"])
# print(dict["city"])

# # loop on dictionary
# for key , value in dict.items():
#     print(f"{key} : {value}")

# dict2 = {}

# dict2["a"] = 1
# dict2["b"] = 2
# dict2["c"] = 3

# print(dict2)

# # list to dictionary
# li = [1,2,3,4,5]
# dict3 = {}
# for x,y in enumerate(li):
#     dict3[x] = y
#     print(dict3)

# # string to dictionary
# str = "hello world"
# dict4 = {}
# for x,y in enumerate(str):
#     dict4[x] = y
#     print(dict4)


# DICTIONARY FUNCTIONS

# dict = {"name":"John","age":30,"city":"New York"}
# dict2 ={"a":"hello"}
# print(dict.keys())
# print(dict.values())
# print(dict.items())
# print(dict.get("name"))
# print(dict.get("age"))
# print(dict.get("city"))
# print(dict.get("country"))
# print(dict.get("country","USA"))
# print(dict.get("country","USA"))
# print(dict.setdefault("e","khurram"))
# print(dict.pop("e"))
# print(dict.popitem())
# print(dict.update(dict2))
# print(dict)
# print(dict.copy())
# print(dict.clear())
# print(dict.fromkeys("hello"))
# print(dict.fromkeys("hello",1))


# ERROR HANDLING:
# try:
#     age = int(input("Enter your age : "))
# except Exception:
#     print("Invalid input")

# print(age)

# try:
#     age = int(input("Enter your age: "))
#     print(age)
# except Exception:
#     print("Invalid input")
# else:
#     print("You are an adult")
# finally:
#     print("Thank you for your input")  # This will run always

