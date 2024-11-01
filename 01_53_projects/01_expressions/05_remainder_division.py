def remainder_division():
    num1 = int (input("\nPlease enter an integer to be divided : "))
    num2 =int (input("\nPlease enter an integer to divide by : "))

    division = num1 // num2 
    remainder = num1 % num2

    print(f"\nThe result of division is \033[1;3m{division}\033[0m with a remainder of \033[1;3m{remainder}\033[0m")

if __name__ == "__main__":
    remainder_division()