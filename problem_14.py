# Problem 14: Check if a number is prime
# Find and fix the error
n = int(input("Enter a number: "))  
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(f"Is {n} prime? {is_prime(n)}")
