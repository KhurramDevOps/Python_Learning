def E_mc2():
    user_input :float = float (input("Enter kilos of mass : "))
    
    print("\ne = m * C^2...")
    m = user_input
    print(f"\nm = \033[1;3m{m}\033[0m kg")

    C = 299792458 
    print(f"\nC = {C} m/s")

    e = m * C ** 2

    print(f"\n\033[1;3m{e}\033[0m joules of energy!")

if __name__ == "__main__":
    E_mc2()
