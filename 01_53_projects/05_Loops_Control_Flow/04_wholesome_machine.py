def wholesome_machine():

    while True:
        affirmation = "\nI am capable of doing anything I put my mind to."
        print(affirmation)
        user_input = input("Please type the above affirmation correctly: ")

        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print("That was not the affirmation. ")

if __name__ == "__main__":
    wholesome_machine()