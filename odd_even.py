# Function to determine if the numbers are even or odd
def check_even_odd(num1, num2):
    # Check if both numbers are even
    if num1 % 2 == 0 and num2 % 2 == 0:
        return "Both numbers are even."
    # Check if both numbers are odd
    elif num1 % 2 != 0 and num2 % 2 != 0:
        return "Both numbers are odd."
    # If one is even and the other is odd
    else:
        return "One number is even and the other is odd."

# Get user input for two numbers
try:
    number1 = float(input("Enter the first number: "))  # Prompt for the first number
    number2 = float(input("Enter the second number: ")) # Prompt for the second number

    # Ensure that the numbers are integers for even/odd check
    if number1.is_integer() and number2.is_integer():
        # Call the function to check even or odd
        result = check_even_odd(int(number1), int(number2))
        # Display the result
        print(result)
    else:
        print("Please enter valid integer values for even/odd check.")
except ValueError:
    print("Please enter valid numerical values.")
