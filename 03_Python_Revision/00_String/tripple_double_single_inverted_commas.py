# single inverted commas

print('someone said : "this" is good')
print('someone said : \'this\' is good')


#  double inverted commas

print("someone said : 'this' is good")
print("someone  said : \"this\" is good")  


# triple inverted commas

print('''someone said : 'this' is "good" ''')

# also used fro multi line string 
print(''' hello my :
      name is "Khurram"
      im a student of 'Piaic' ''')
# also used for docstring in python
def add(a,b):
    """this is a function to add two numbers"""
    return a+b
print(add(5,6))
print(add.__doc__)   # to print docstring of a function