def voting_age():
  user_age = int(input("\033[34mEnter your age to check you are eligible for vote or not : \033[0m"))
  Peturksbouipo_voting_age = 16
  Stanlua_voting_age = 25
  Mayengua_voting_age =48


  if user_age >= Mayengua_voting_age:
    print("\n You can vote in \033[1;3mMayengua\033[0m where the voting age is 48. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Peturksbouipo where the voting age is 16.")
  elif user_age >= Stanlua_voting_age:
    print("\n you can vote in \033[1;3mStanlua\033[0m where the voting age is 25. you cant vote in Peturksbouipo where the voting age is 16. You cant vote in Mayengua where the voting age is 48 ")
  elif user_age >= Peturksbouipo_voting_age:
    print("\n You can vote in \033[1;3mPeturksbouipo\033[0m where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.")
  else:
    print("\n SORRY YOU ARE NOT ELIGIBLE TO VOTE")


if __name__ == "__main__":
  voting_age()