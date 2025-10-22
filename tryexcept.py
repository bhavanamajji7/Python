# Program to demonstrate error handling using try-except

try:
    # Take input from the user
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    # Attempt division
    result = numerator / denominator

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

except ValueError:
    print("Error: Please enter only numeric values.")

finally:
    print("Program execution completed.")
