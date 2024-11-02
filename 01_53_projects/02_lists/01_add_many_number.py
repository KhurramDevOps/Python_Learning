def add_many_numbers(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

def list():
    numbers = [1,3,5,6,7,2,8]
    add_numbers = add_many_numbers(numbers)
    print(add_numbers)

if __name__ == "__main__":
    list()