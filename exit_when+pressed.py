while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")  # Prompt for a number

    if user_input.lower() == 'exit':  # Check if the user wants to exit
        print("Exiting the program. Goodbye!")
        break  # Exit the loop

    try:
        # Convert input to float
        number = float(user_input)

        # Determine the type of the number
        number_type = determine_number_type(number)

        # Display the result
        print(f"The number you entered is {number_type}.")
    except ValueError:
        print("Please enter a valid numerical value.")

