def print_one_digit(num:int):
    remainder = num % 10
    return remainder

def main():
    user_input = int(input("\033[34mEnter a number : \033[0m"))
    print(f"The one's digit is {print_one_digit(user_input)}")

if __name__ == "__main__":
    main() 
