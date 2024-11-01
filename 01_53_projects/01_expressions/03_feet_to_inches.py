def feet_to_inches():
    user_input :float = float (input("Write feet here to convert in inches : "))
    inches_in_foot = 12
    in_inches = user_input * inches_in_foot

    print(f"\nThe \033[1;3m{user_input}\033[0m feet is converted in \033[1;3m{in_inches}\033[0m inches")

if __name__ == "__main__":
    feet_to_inches()