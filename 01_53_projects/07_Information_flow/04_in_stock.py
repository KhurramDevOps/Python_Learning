def in_stock(f):
    inventory = {"apple":25,"mango":300,"peer":500,"orange":1000}
    if f in inventory:
        return f"This fruit is in Stock! Here is how many : {inventory[f]}"
        
    return f"This fruit is not in Stock"

def main():
    fruit = input("\033[1;3mEnter a fruit : \033[0m")
    print(in_stock(fruit))

if __name__ == "__main__":
    main()