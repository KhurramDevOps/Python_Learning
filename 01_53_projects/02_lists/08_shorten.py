Max_length = 3 

def shorten(x):
    while True:
        if len(x) > Max_length:
            print(x.pop())
        else :
            print(f"The length of list is unchanged cuz its equal to or shorter than Max length : {x}")
        if len(x) == Max_length:
            break
    return x
    

def list_length():
    my_list = [1,2,3,4,5,6,7,8,9]
    short_list = shorten(my_list)
    print(f"This is the Shortened List : \033[1;3m{short_list}\033[0m")

if __name__ == "__main__":
    list_length()