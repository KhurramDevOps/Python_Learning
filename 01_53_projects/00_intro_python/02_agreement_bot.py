def fav_animal():
    user_input = str(input(f"What's your favorite animal? : "))
    # bold_italic = f"\033[1;3m{user_input}\033[0m"
    # print(bold_italic)
    print(f"\nMy Favorite Animal is also \033[1;3m{user_input}\033[0m! ")

    
if __name__ == "__main__":
    fav_animal()




