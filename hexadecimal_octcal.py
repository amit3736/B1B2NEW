# Function to convert an integer to binary, octal, and hexadecimal
def convert_number(num):
    # Initialize empty strings for binary, octal, and hexadecimal
    binary = ""
    octal = ""
    hexadecimal = ""

    # Convert to binary using bitwise operators
    for i in range(31, -1, -1):  # Loop from 31 to 0 for a 32-bit representation
        if num & (1 << i):  # Check if the ith bit is set
            binary += "1"
        else:
            binary += "0"

    # Remove leading zeros from binary representation
    binary = binary.lstrip("0") or "0"  # Ensure at least one '0' if the number is 0

    # Convert to octal using bitwise operators
    temp_num = num
    while temp_num > 0:
        octal = str(temp_num & 7) + octal  # Get the last 3 bits (octal digit)
        temp_num >>= 3  # Right shift by 3 bits to process the next octal digit

    # If the number is 0, set octal to "0"
    if num == 0:
        octal = "0"

    # Convert to hexadecimal using bitwise operators
    temp_num = num
    while temp_num > 0:
        hex_digit = temp_num & 15  # Get the last 4 bits (hexadecimal digit)
        if hex_digit < 10:
            hexadecimal = str(hex_digit) + hexadecimal  # Convert to string
        else:
            hexadecimal = chr(hex_digit - 10 + ord('A')) + hexadecimal  # Convert to A-F
        temp_num >>= 4  # Right shift by 4 bits to process the next hex digit

    # If the number is 0, set hexadecimal to "0"
    if num == 0:
        hexadecimal = "0"

    return binary, octal, hexadecimal

# Get user input
try:
    number = int(input("Enter an integer: "))  # Prompt for an integer

    # Convert the number and get its representations
    binary_rep, octal_rep, hex_rep = convert_number(number)

    # Display the results
    print(f"Binary: {binary_rep}")
    print(f"Octal: {octal_rep}")
    print(f"Hexadecimal: {hex_rep}")
except ValueError:
    print("Please enter a valid integer.")

