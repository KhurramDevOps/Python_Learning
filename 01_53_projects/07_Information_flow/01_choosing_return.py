ADULT_AGE = 18 

def is_adult(age):
    if age >= ADULT_AGE:
        print("True")
    else:
        print("False")

def main():
    user_input = int(input("Enter your age : "))
    is_adult(user_input)

if __name__ == "__main__":
    main()
