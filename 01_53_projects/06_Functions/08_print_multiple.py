def print_multiple(message , times):
    multiples = message * times
    return multiples

def main():
    user_message = input("\033[34mEnter a message : \033[0m")
    user_times = int(input("\033[34mEnter a number how many times to repeat a text : \033[0m"))
    print(f"\n{print_multiple(user_message,user_times)}")

if __name__ == "__main__":
    main()