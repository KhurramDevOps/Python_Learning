# FILE HANDLING 

# WHAT IS FILE HANDLING?
# File handling is a process of reading and writing data to a file. It is a way to
# store and retrieve data in a structured format.
# File handling is used to store data in a file and retrieve it when needed.
# It is a way to store data in a file and retrieve it when needed.

# example :

# r:
# r for reading the file

file = open("file.txt", "r")
print(file.read())
file.close()

# w:
# w for writing the file if 
# the file does not exist it will create a new file
# if their is content in file it will delete the content and write the new content

w = open("file.txt", "w")
w.write("Hello, world!")
w.close()

r = open ("file.txt", "r")
print(r.read())
r.close()

w = open("file5.txt","w")
w.write("new file created ")
w.close

# a:
# a for appending the file
# if the file does not exist it will create a new file
# if their is content in file it will add the new content at the end of the file

a = open("file.txt","a")
a.write("\nThis is second data")
a.close()

# r+:
# r+ for reading and writing the file
# if the file does not exist it will create a new file
# if their is content in file it will delete the content and write the new content

r = open("file.txt","r+")
r.write("this is written using r+")
r.seek(0)  #seek is used to move the cursor to the beginning of the file
content = r.read()
r.close()
print(content)

# w+:
# w+ for writing and reading the file
# if the file does not exist it will create a new file
# if their is content in file it will delete the content and write the new content

write_plus = open("file.txt","w+")
write_plus.write("this is written using w+")
write_plus.seek(0)
content = write_plus.read()
write_plus.close()

# a+:
# a+ for appending and reading the file
# if the file does not exist it will create a new file
# if their is content in file it will add the new content at the end of the file

with open("file.txt","a+") as y:
    y.write("\nthis is written using a+")
    y.seek(0)
    y.read()
    y.seek(0)


# with open() :
#  is used to open the file and close the file automatically
#  it is used to prevent memory leak
#  it is used to prevent file not closed error

with open("file5.txt","w+") as f:
    f.write("this is written using with open()")
    f.seek(0)
    content1 = f.read()
    print(content) 

