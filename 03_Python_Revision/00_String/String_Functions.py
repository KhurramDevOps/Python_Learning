# STRING FUNCTIONS 
# STRING IS IMMUTABLE
# EXAMPLE 
string = "Hello world"
string2= string.upper()
print(string)  # prints Hello world cuz when we add a function it makes a new copy string where the function is  applied but the original string not changed
print(string2)

# upper()
name1 = "Khurram Shahzad"
print(name1.upper())

age1 = "Eighteen"
print(age1.upper())

# lower()
name2 = "Khurram Shahzad"
print(name2.lower())
age2 = "Eighteen"
print(age2.lower())

# title()
name3 = "khurram shahzad"
print(name3.title())
age3 = "eighteen"
print(age3.title())

# capitalize()
name4 = "khurram shahzad"
print(name4.capitalize())

# swapcase()
thing = "CHaiR"
print(thing.swapcase())

# center()
car = "Nissan"
print(car.center(20))
print(car.center(20,"*"))

# count()
bike = "Kawasaki"
print(bike.count("a"))

# endswith()
animal = "lion"
print(animal.endswith("n"))

print(animal.endswith("e"))

# expandtabs()
plant ="sun\tflower"
print(plant.expandtabs(6))

# find()
# find and index work similarly but if the word is not exist the find give you -1 amd  index give you value error
place = "lahore a"
print(place.find("a"))
print(place.find("a",2)) #with this u also find the index of same  character in string
print(place.find("z"))

# join()
things = "bed table"
print(" ".join(things))

# SECOND WAY TO USE join()
li = list(things)
print(li)
my_string = ''.join(li)
print(my_string) 

# Task
name = "khurram"
my_list = list(name)
my_list.pop()
print(my_list)
my_string = "".join(my_list)
print(my_string)

# strip
text = "   hello   "
print(text.strip())

# lstrip
msg = "   bye"
print(msg.lstrip())

# rstrip
message = "hy     "
print(message.rstrip())