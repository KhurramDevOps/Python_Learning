# LOGICAL OPERATORS 
# 1. AND (&&)
# 2. OR (||)
# 3. NOT (!)

# EXAMPLE 

# 1. AND (&&)
#   - Returns true if both conditions are true
#   - Returns false if either condition is false
#   - Returns false if both conditions are false
#   - Returns true if one condition is true and the other is false
#   - Returns true if one condition is true and the other is false

# 2.  OR (||)
#   - Returns true if either condition is true
#   - Returns false if both conditions are false
#   - Returns true if one condition is true and the other is false
#   - Returns true if one condition is true and the other is true
#   - Returns true if both conditions are true

# 3.  NOT (!)
#   - Returns true if the condition is false
#   - Returns false if the condition is true
#   - Returns false if the condition is false
#   - Returns true if the condition is true

# Example with code 

# AND (&&)
a = 10 
b = 20
print(a > 5 and b > 5) # True
print(a > 5 and b < 5) # False
print(a < 5 and b > 5) # False

# OR  (||)
print(a > 5 or b > 5) # True
print(a > 5 or b < 5) # True
print(a < 5 or b < 5) # False

# NOT  (!)
print(not a > 5) # False
print(not a < 5) # True
print(not a == 5) # True
print(not a != 5) # False