# STRING 
# WHAT IS STRING 
# ANYTHING WRITTEN INSIDE INVERTED COMMAS IS CALLED STRING 
# STRING IS USED TO STORE TEXT DATA

datatype = "Khurram is a good student"
print(datatype)
print(type(datatype))


# INDEXING , SLICING ,STEPPING

# INDEXING 
#  POSITIVE INDEXING
name = "Khurram shahzad"
print(name[11])

age = "eighteen"
print(age[3])

# NEGATIVE INDEXING
print(name[-1])
print(name[-6])

print(age[-4])
print(age[-5])

# SPACE ALSO TAKE INDEX

# SLICING 
# SLICING IS USED TO GET THE PART OF THE STRING
# POSITIVE SLICING
city = "Lahore is beautiful"
print(city[0:5])
print(city[0:7])
print(city[0:10])
print(city[:])

# NEGATIVE SLICING
province = "Punjab is the province of pakistan" 
print(province[-10:])
print(province[-15:])
print(province[-20:])
print(province[-1:])

# STEPPING
# STEPPING IS USED TO GET THE PART OF THE STRING WITH A CERTAIN STEP
# POSITIVE STEPPING

thing = "chair table bed"
print(thing[0:7:2])
print(thing[0:7:3])
print(thing[0:12:4])
print(thing[::1])

# NEGATIVE STEPPING
print(thing[::-1])
print(thing[::-2])
print(thing[::-4])


# TASK 
intro = "My name is Khurram and My age is 18 and my Qualification is inter"
for x,y in enumerate(intro):
    print(f"{x} : {y}")
print(intro[11:19], end = " ")
print(intro[33:35], end=  " ")
print(intro[60:])

numbers = "123456789"
print(numbers[1::2])
