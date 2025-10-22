# Fibonacci series up to n terms

# Take input from the user
n = int(input("Enter the number of terms: "))

# First two terms of Fibonacci sequence
a, b = 0, 1
count = 0

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence up to", n, "term:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a, end=" ")
        c = a + b   # next term is the sum of the previous two
        a = b       # update first term
        b = c       # update second term
        count += 1
