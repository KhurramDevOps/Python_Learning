import random
def done():
    
    return random.random() < 0.1 #10 percent change of returning true

def chaotic_counting():
    for i in range(1,11):
        if done():
            print("I'm Done. ")
            return
        print(i)   
        
if __name__ == "__main__":
    print("Im going to count until 10 or until I feel like stopping. ")
    chaotic_counting()


