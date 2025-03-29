
# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

def main():
    try:
        # Get the numbers we want to divide
        dividend = int(input("Please enter an integer to be divided: "))
        divisor = int(input("Please enter an integer to divide by: "))

        # Check if divisor is zero
        if divisor == 0:
            print(f"Error: {dividend} Cannot be divide by zero.")
        else:
            # Integer division quotient only, no decimal part
            quotient = dividend // divisor

            # this gets the remainder
            remainder = dividend % divisor

            # the result
            print(f"The result of this division is {quotient} with a remainder of {remainder}")

    except ValueError:
        print("Error: Please enter valid integers.")

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()