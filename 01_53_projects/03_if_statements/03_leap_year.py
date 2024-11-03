def leap_year():
    user_input = int(input("\033[34mEnter the year to check its leap year or Not : \033[0m"))
    
    if user_input % 400 == 0 and user_input % 100 == 0 :
            print(f"\n\033[1;3m{user_input}\033[0m : is a leap year")
    elif user_input % 100 == 0 and user_input % 400 != 0:
         print(f"\n\033[1;3m{user_input}\033[0m : is not a leap year")
    elif user_input % 4 == 0 :
        print(f"\n\033[1;3m{user_input}\033[0m :  is a leap year")
    else:
        print(f"\n\033[1;3m{user_input}\033[0m : is Not a leap year ")

if __name__ == "__main__":
    leap_year()