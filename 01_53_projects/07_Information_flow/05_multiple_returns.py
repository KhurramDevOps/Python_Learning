def multiple_returns(x,y,z):
  
    return x,y,z

def main():
    first_name = input("Enter your first name : ")
    last_name = input("Enter your last name : ")
    while True:
        email = input("Enter you email address : ")

        if not email.endswith("@gmail.com") :
            print("Please enter  valid email which endswith (@gmail.com) ")
        else:
            break
      
    print(f"Received the following User Data {multiple_returns(first_name,last_name,email)}")

if __name__ == "__main__":
    main()