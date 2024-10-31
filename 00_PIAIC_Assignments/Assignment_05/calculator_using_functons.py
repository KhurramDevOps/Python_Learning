def sum (x:int, y:int) -> int:
    """Addition of numbers"""
    return x + y

def sub (x:int, y:int) -> int:
    """Subtraction of numbers"""
    return x - y

def mul (x:int, y:int) -> int:
    """Multiply of numbers"""
    return x * y

def divide (x:int, y:int) -> (float | str):
    """Division of numbers"""
    if y == 0:
        return "The number divided by Zero is Invalid"
    else:
        return (x / y)
    
def square (x:int ) -> int:
    """Square of number"""
    return x ** 2

num1 = int(input("Enter the first number: "))
choice = input("choose the following operator: '+','-','*','/','**' ")

if choice in  ['+','-','*','/'] :
    num2 = int(input("Enter the second number: "))
if choice == '+':
    print(sum(num1,num2))
elif choice == '-':
    print(sub(num1,num2))
elif choice == '*':
    print(mul(num1,num2))
elif choice == '/':
    print(divide(num1,num2))
elif choice == '**':
    print(square(num1))
else:
    print("INVALID CHOICE")
    

