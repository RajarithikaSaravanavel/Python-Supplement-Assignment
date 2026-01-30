# Problem 12: Print multiplication table
# Find and fix the error

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
