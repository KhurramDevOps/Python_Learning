from hashlib import sha256

def hashing(x):
    converting_password = sha256(x.encode()).hexdigest()
    return converting_password


def login(email,password):
   stored_passwords = {
    "khurram@gmail.com":"5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
    "ali@gmail.com":"973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
    "bob@gmail.com":"882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
   }
   if email in stored_passwords:
    stored_hash = stored_passwords[email]
    user_hash = hashing(password)
    if stored_hash == user_hash:
        print("Login Successful! ")
    else:
        print("Incorrect password! ")
   else:
    print("User not found! ")

def main():
    user_input = input("Enter your email to login : ")
    user_input1 = input("Enter your password to login : ")

    login(user_input,user_input1)

if __name__ == "__main__":
    main()    

