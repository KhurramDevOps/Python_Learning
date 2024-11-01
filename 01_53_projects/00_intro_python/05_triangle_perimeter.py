def triangle_perimeter():
    user_input = float (input("What is the length of side 1 : "))
    user_input1 = float (input("\nWhat is the length of side 2 : "))
    user_input2 = float (input("\nWhat is the length of side 3 : "))

    perimeter_of_triangle = user_input + user_input1 + user_input2

    print(f"\nThe perimeter of triangle is \033[1;3m{perimeter_of_triangle}\033[0m")
    
if __name__ == "__main__":
    triangle_perimeter()