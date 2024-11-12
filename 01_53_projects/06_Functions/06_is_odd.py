def checking_odd_even():
    for i in range(10):
        if is_odd(i):
            print(f"{i} is odd,",end=" ")
        else:
            print(f"{i} is even,",end=" ")



def is_odd(a :int):
    
    remainder = a % 2
    return remainder == 1

if __name__ == "__main__":
    checking_odd_even()