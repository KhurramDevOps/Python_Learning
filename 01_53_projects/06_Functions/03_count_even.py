def even(a):
    even_numbers_total = 0
    for i in a:
        if i % 2 == 0:
            even_numbers_total += 1
    print(f"Total even number are : {even_numbers_total}")


def count_even():
    li = []
    while True:
        user_input = input("Enter an integer or press enter to stop : ")
       
        if user_input == "":
            break
        else:
            li.append(int(user_input))

    even(li)
    
if __name__ == "__main__":
    count_even()