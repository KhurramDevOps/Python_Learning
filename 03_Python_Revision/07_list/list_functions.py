# FUNCTIONS OF LIST

# 1. append() : This function is used to add an element to the end of list
# append return  None
# Example

my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)  

my_list.append(7)
print(my_list)

# 2. insert() :  This function is used to add an element at a specified position in list
# insert  return  None
# Example

li = ["a","b","c"]
li.insert(1,"d")
print(li)

li.insert(2,4)
print(li)

# 3. extend()  : This function is used to add multiple elements to the end of list
# extend return  None
# Example

my_list.extend(li)
print(my_list)

my_list.extend([7,8,9])
print(my_list)

# 4.  remove() : This function is used to remove the first occurrence of the specified element from the list
# remove  return  None
# Example

my_list.remove("a")
print(my_list)

my_list.remove(4)
print(my_list)

# 5.  pop() : This function is used to remove and return the element at the specified position in the list
# pop have return  value
# Example

my_list.pop()
print(my_list)

my_list.pop(1)
print(my_list)

# 6. clear() :  This function is used to remove all elements from the list
# clear return  None
# Example

my_list.clear()
print(my_list)

# 7. del() :  This function is used to delete the element at the specified position in the list
# del return  None
# Example

del li[4]
print(li)

del li[3]
print(li)
# del function works everywhere

# 8. count() : this function is used to  count the number of occurrences of the specified element in the list
# count return  value
# Example
li2 = [1, 2, 3, 4, 5, 5,6,6,6,6]
li2.count(6)
print(li2)

li2.count(5)
print(li2)


# 9. copy() :  This function is used to create a copy of the list
# copy return  value
# Example

li3 = li.copy()
print(li3)

# 10. sort() : This function  is used to sort the list in ascending order
# sort return  None
# Example

li4 = [1,2,3,9,8,4,2,7]
li4.sort()
print(li4)

li4.sort(reverse=True)
print(li4)

# 11. reverse() : This function is  used to reverse the list
# reverse return  None
# Example

li5 = [1,2,3,4,5]
li5.reverse()
print(li5)


# 12. index() : This function is used to return the index of the first occurrence of the specified element
# index return  value
# Example

li6 = [1,2,3,4,5]
index =li6.index(5)
print(index)

# 13. max () : This function is used to return the maximum element in the list
# max return  value
# Example
li7 = [1,2,3,4,5]
max = max(li7)
print(max)


# 14. min () : This function is used to return the minimum element in the list
# min return  value
# Example

li8 = [1,2,3,4,5]
min = min(li8)
print(min)
