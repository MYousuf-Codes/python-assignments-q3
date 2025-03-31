# Print 10 random numbers in the range 1 to 100.
# The random numbers should not be repeated.
# Recall that the python random library has a function randint which returns an integer in the range set 
# by the parameters (inclusive). For example this call would produce a random integer between 1 and 6, 
# which could include 1 and could include 6:
#value = random.randint(1, 6)

import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    Generates and prints 10 random numbers between 1 and 100 using if statements.
    """
    random_numbers = []  # Initialize an empty list

    count = 0  # Count to keep track of how many numbers have been generated
    while count < N_NUMBERS:
        number = random.randint(MIN_VALUE, MAX_VALUE)  # Generate a random number

        if number >= MIN_VALUE and number <= MAX_VALUE:  # Check if it is within range
            random_numbers.append(number)  # Add to the list
            count += 1  # Increment the cont

    # Print the numbers separated by spaces
    print(" ".join(map(str, random_numbers)))

if __name__ == '__main__':
    main()
