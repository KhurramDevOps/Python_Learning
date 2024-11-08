# FUNCTIONS OF DICTIONARY

# 1. clear()  : This function is used to remove all items from the dictionary.
# clear return None
# Example:

d = {'a': 1, 'b': 2, 'c': 3}
print(d.clear())  

# 2. fromkeys() : This  function is used to create a new dictionary with keys from sequence.
# fromkeys () return dictionary
# Example:
fruits = ['apple', 'banana', 'cherry']
my_dict = dict.fromkeys(fruits, 5)
print(my_dict)

tu = (1,2,3,4,5)
my_dict = dict.fromkeys(tu, 5)
print(my_dict)

# 3. get() :  This function is used to get the value of a key if it exists in the dictionary.
# get() return value of key if key exists in dictionary otherwise return default value
# Example: 

dict1 =  {'a': 1, 'b': 2, 'c': 3}
print(dict1.get('c'))
print(dict1.get('d', "Not found"))

# 4. pop() :  This function is used to remove the item for a given key and return its value.
# pop() return value of key if key exists in dictionary otherwise return default value
# Example:

dict1 =  {'a': 1, 'b': 2, 'c': 5}
print(dict1.pop('c'))
print(dict1.pop('d', "Not found"))
print(dict1.pop('a'))

print(dict1.popitem()) # if you dont give value it will remove  last item from dictionary


# 5. copy():  This function is used to create a copy of the dictionary.
# copy() return dictionary
# Example:
dict2 = {1:"a",2:"b",3:"c"}
dict3 = dict2.copy()
print(dict3)


# 6. update() :   This function is used to update the dictionary with the items from another dictionary or from an iterable of
# key-value pairs.
# update() return None
# Example:

d1 = {1: '001', 2:"002",3:"003"}
d2 = {4:"004",4:"004",5:"005"}
d1.update(d2)
print(d1)

d3 =  {1:"006",2:"007"}
d1.update(d3)
print(d1) # it will change the value of key if the key  is same in both dictionary


# 7. setdefault() : This function is used to set a default value for a key if it is not already present in the dictionary.
# set default return  value of key if key exists in dictionary otherwise return default value
# Example:
d1 = {1:"a",2:"b",3:"c"}
print(d1.setdefault(1))
print(d1.setdefault(4,"g")) # if not found it will add the given key value in  dictionary
print(d1)

