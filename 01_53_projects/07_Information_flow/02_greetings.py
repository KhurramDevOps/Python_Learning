def greet(name):
    return f"Greetings {name}!"

def main():
    user_input = input("Enter your name : ")
    print(greet(user_input))

if __name__ == "__main__":
    main()