def double_it():
    user_input = int(input("Enter the number you want to double : "))

    while user_input <= 100:
        user_input *= 2
        print(user_input,end=" ")


if __name__ == "__main__":
    double_it()