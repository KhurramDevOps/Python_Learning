LOW = 5
HIGH = 35

def in_range(n,low,high):
    """ Returns True if n is between low and high,
      inclusive. high is guaranteed to be greater than low. """
    
    if n >= low and n <= high:
        return "True"
    
    return "False"

def main():
    user_input = int(input("Enter a number : "))
    print(in_range(user_input,LOW,HIGH))

if __name__ == "__main__":
    main()
