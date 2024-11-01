import math
def pythagorean_theorem():
    length_of_AB = float (input("Enter the length of AB : " ))
    length_of_AC = float (input("\nEnter the length of AC : "))
    
    length_of_BC = math.sqrt(length_of_AB ** 2 + length_of_AC ** 2)

    print(f"\nThe Length of BC (The Hypotenuse) is : \033[1;3m{length_of_BC}\033[0m")


if __name__ == "__main__":
    pythagorean_theorem()