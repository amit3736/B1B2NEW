#modifying the rectangle area program
#using format method

try:
    length = float(input("Enter the length of the rectangle: "))  # Prompt for length
    width = float(input("Enter the width of the rectangle: "))    # Prompt for width

    # Calculate the area
    area = calculate_area(length, width)

    # Display the result formatted to two decimal places
    print("The area of the rectangle is: {:.2f} square units".format(area))
except ValueError:
    print("Please enter valid numerical values for length and width.")
