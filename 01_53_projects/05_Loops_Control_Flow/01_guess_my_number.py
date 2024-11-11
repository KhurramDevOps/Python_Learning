import random
my_number = random.randint(0,100)

def guess_my_number():
    
        guess = int(input("I am thinking of a number between 0 and 99... Enter a guess : "))
        while guess != my_number:  
        
           
            if guess > my_number:
                print("Your guess is too high")
            elif guess < my_number:
                print("Your guess is too low")
            else:
                print("enter a number between 0 and 99")

            guess =int(input("\nEnter a New guess : "))
        print(f"{guess}Congrats! The number was:{my_number} ")
            
if __name__ == "__main__":
    guess_my_number()