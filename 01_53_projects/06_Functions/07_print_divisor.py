# way 1

def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(num):
        curr_divisor = i + 1
        if num % curr_divisor == 0:
            print(curr_divisor)

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)



if __name__ == '__main__':
    main()

# way2 
import math
def print_divisor(num:int):
    li = []
    square_root = int(math.sqrt(num)) + 1
    for i in range(1,square_root):
        if num % i == 0:
            li.append(i)
            li.append(num // i) 
    li.sort()
    return li

def main():
    user_input = int(input("Enter a number : "))
    divisors = print_divisor(user_input)
    print(f"Here the divisors of {user_input} : {divisors}")
    
if __name__ == "__main__":
    main()

