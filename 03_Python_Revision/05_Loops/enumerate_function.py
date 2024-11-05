# ENUMERATE FUNCTION
# The enumerate function returns a tuple containing a count (from start which defaults to 0) and

# EXAMPLE 

name = "khurram"

for index , char in  enumerate(name):
    print(f" {index} : {char}")

sentence = "my name is khurram"
for index ,  word in enumerate(sentence):
    print(f" {index} : {word}")

    
# TASK
# for i in range(1,11):
#     print(f" 2  x {i} = {2 * i}") 