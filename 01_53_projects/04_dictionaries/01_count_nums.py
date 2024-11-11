my_dict = {}
def count_nums():
 
 while True:
  user_input = input("\033[34mEnter a number or press enter to stop : \033[0m")
  if user_input == "":
   break
 
  num = int(user_input)
  if num in my_dict:
   my_dict[num] += 1
  else:
   my_dict[num] = 1

 for i , x in my_dict.items():
    print(f"{i} appears, {x} times")

if __name__ == "__main__":
    count_nums()
