import random 
def dice_simulator():

    dice = range(1,7)

    die1_first_roll = random.choice(dice)
    die2_first_roll = random.choice(dice)

    print(f"\nThe number obtained by die1 first time is \033[1;3m{die1_first_roll}\033[0m ")
    print(f"\nThe number obtained by die2 first time is \033[1;3m{die2_first_roll}\033[0m")

    die1_second_roll = random.choice(dice)
    die2_second_roll = random.choice(dice)

    print(f"\nThe number obtained by die1 second time is \033[1;3m{die1_second_roll}\033[0m ")
    print(f"\nThe number obtained by die2 second time is \033[1;3m{die2_second_roll}\033[0m")

    die1_third_roll = random.choice(dice)
    die2_third_roll = random.choice(dice)

    print(f"\nThe number obtained by die1 third time is \033[1;3m{die1_third_roll}\033[0m ")
    print(f"\nThe number obtained by die2 third time is \033[1;3m{die2_third_roll}\033[0m ")

if __name__ == "__main__":
    dice_simulator()