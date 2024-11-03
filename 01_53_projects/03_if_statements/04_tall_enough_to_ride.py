def tall_enough_to_ride():
    condition = True
    while condition:
        user_height =  (input("\033[1;3mEnter your Height in inches (or press Enter to stop) : \033[0m"))
        normal_height = 50  #inches
        try:
            if user_height == "":
                break
            elif float(user_height) >= float(normal_height):
                print("\nYou're tall enough to ride. ")
            else:
                print("\nYou're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("\nINVALID INPUT , Please enter a valid number .")

            
if __name__ == "__main__":
    tall_enough_to_ride()
