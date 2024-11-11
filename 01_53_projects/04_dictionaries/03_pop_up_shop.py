def pop_up_shop():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0
    for x,y in fruits.items():

        user_input = int(input(f"\033[1;3mHow many {x} you want to buy : \033[0m"))
        total_cost += user_input * y

    print(f"Your total is ${total_cost}")

if __name__ == "__main__":
    pop_up_shop()