# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

# For example if the user enters the number 2 you would then print:

# 4 8 16 32 64 128

def main():
    """
    Asks the user for a number, then repeatedly doubles it until it reaches 100 or more.
    """
    curr_value = int(input("Enter a number: "))  # Get user input

    while curr_value < 100:  # Continue doubling until 100 or more
        print(curr_value, end=" ")  # Print the current value
        curr_value *= 2  # Double the value

    print(curr_value)  # Print the final value that exceeds 100

if __name__ == '__main__':
    main()
