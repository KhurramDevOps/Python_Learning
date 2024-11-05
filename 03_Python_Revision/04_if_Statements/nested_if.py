# # NESTED IF 
# # WHAT IS NESTED IF?


# # EXAMPLE 

# i = 10
# if i == 10 :
#     print("parent if")
#     if i > 5:
#         print("child if")
#     else:
#         print("child else")
# else :
#     print("parent else")

# temperature = 25  # temperature in Celsius
# humidity = 60     # humidity percentage

# if temperature > 20:
#     print("It's warm outside.")
    
#     if humidity > 50:
#         print("It's also humid.")
#     else:
#         print("The air is dry.")
# else:
#     print("It's cool outside.")


# i = 10 
# if(i == 10):
#     print("parent if ")
#     if(i < 5):
#         print("child if ")
#         if(i > 5):
#             print("childesh if")
#     else:
#         print("child else")
        
# else:
#     print("parent else")

# TASK 
marks = int(input("Enter your marks : "))
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks  >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif  marks >= 50:
    print("Grade E")
else:
    print("fail") 