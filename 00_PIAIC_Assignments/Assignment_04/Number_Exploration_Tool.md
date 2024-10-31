# Assignment No 6 Markdown file

## Step 1

### Create a empty list and ,Ask the user for input their name

```python
num_list = []
user_name =  input("Please enter your name: ")
print ()
```

Explain code.

1. FIrst we create a empty list
2. Ask the user for input their name
3. Print a blank line

## Step 2

### Ask the user for three favorite numbers and collect them in a list.

```python
for x in range(1,  4):
    user_number : int = int(input(f"Please enter your {x} favorite number : "))
    num_list.append(user_number)
    print(num_list)
```

#### Explain code.

- Ask the user for three favorite numbers
- Collect them in a list
- Print the list after each input
- Use a for loop to repeat the process 3 times

## Step 3

### Display each number and its square.

```python
for num in num_list:
    print(f"The number {num} and its square is : ({num}, {num ** 2})")
```

#### Explain code.

We use a for loop to iterate over each number in the list.Then we using f-string to print the number and its square.

## Step 4

### Sum of favorite number.

```python
sum_of_number = sum(num_list)
print(f"\nWonderful! The sum of your favorite numbers is : {sum_of_number}")
```

#### Explain code.

We use the built-in function sum() to calculate the sum of all numbers in the list.Again we use f-string to print the result with the statement.

## Step 5

### Determine the sum of numbers is a Prime number or not.

```python
Is_prime =  True
if sum_of_number <= 1:
    Is_prime = False
for i in range(2,sum_of_number):
    if sum_of_number % i == 0:
        Is_prime = False

if Is_prime:
    print(f"Wow! The number  {sum_of_number} is a prime number")
else:
    print(f"Sorry, the number {sum_of_number} is not a prime number")
```

#### Explain code.

We first check if the sum is less than or equal to 1, if so, it is not a prime number. Then we use a for loop to check if the sum is divisible by any number between 2 and the sum itself. If it is, then it is not a prime number. If it is not divisible by any of these numbers, then it is a prime number. We use a flag variable Is_prime to track whether the sum is a prime number or not.
We use if -else statement to print the result.

![output of code](https://imgur.com/a/AbcXBxh)
