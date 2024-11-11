def double(x):
    return x * 2

def main():
    user_input = int(input("\033[1;3mEnter a number : \033[0m"))
    doubling = double(user_input)
    print(f"{user_input} Double that is {doubling}")

if __name__ == "__main__":
    main()

