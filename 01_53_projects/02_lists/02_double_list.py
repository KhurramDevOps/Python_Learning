def double_list():
    numbers : list = [1,2,3,4]
    doubled_list =  []
    for i in numbers:
        doubled_list.append(i * 2)
    numbers.clear()
    numbers.extend(doubled_list)
    print(numbers)
   
if __name__ == "__main__":
    double_list()

# SECOND WAY

def double_list():
   numbers = [1,2,3,4]
   numbers = [ num * 2 for num in numbers]
   print(numbers)

if __name__ == "__main__":
    double_list()

# THIRD WAY 

def double_list():
   numbers = [1,2,3,4]
   for i in range(len(numbers)):
       numbers[i] *= 2
   print(numbers)

if __name__ == "__main__":
    double_list()