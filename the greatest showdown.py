def find_largest_and_smallest():
    """
    Prompts the user to enter three numbers.
    Identifies and prints out the largest and smallest numbers among the three.
    """
    # Prompt the user to enter three numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Find the largest number
    largest = max(num1, num2, num3)
    # Find the smallest number
    smallest = min(num1, num2, num3)

    # Print out the results
    print(f"The largest number is: {largest}")
    print(f"The smallest number is: {smallest}")

# Call the function to test it
find_largest_and_smallest()
