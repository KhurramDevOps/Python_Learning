def get_list():
    my_list = []
    condition = True
    while condition:
        user_input = input("\n\033[34mEnter a value (or just Enter to stop) : \033[0m")
        
        if user_input == "":
            condition = False
        else:
            my_list.append(user_input)
    print(f"\nHere's the list : \033[1;3m{my_list}\033[0m")

if __name__ == "__main__":
    get_list()