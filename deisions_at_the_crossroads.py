def check_number():
    """
    Prompts the user to enter a number and determines if the number is positive, zero, or negative.

    This function:
    - Takes user input and attempts to convert it to an integer.
    - Checks if the input number is positive, zero, or negative.
    - Prints a corresponding message based on the input value.
    - Handles ValueError exceptions if the user input is not a valid integer.
    """
    try:
        number = int(input("Enter a number: "))
        
        if number > 0:
            print("The number is positive")
        elif number == 0:
            print("The number is zero")
        else:
            print("The number is negative")
    except ValueError:
        print("Please enter a valid number.")

# Call the function to test it
check_number()

