# Problem 16: Find the second largest number in a list
# Find and fix the error

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
numbers.sort()
second_largest = numbers[-2]
print(f"Second largest: {second_largest}")
