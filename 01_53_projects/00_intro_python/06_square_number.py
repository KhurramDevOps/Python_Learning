def square():
    user_input :float = float (input("Type a number to see its square : "))
    print(f"\033[1;3m{user_input}\033[0m squared is \033[1;3m{user_input ** 2}\033[0m")

if __name__ == '__main__':
    square() 
