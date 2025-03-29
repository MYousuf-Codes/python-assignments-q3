# Write a program which asks the user how tall they are and prints whether or not 
# they're taller than a pre-specified minimum height.

# In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently 
# have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like

# (For an extra challenge, write code which will repeatedly ask a user how tall they are and tell them whether or not 
# they're tall enough to ride, until the user doesn't enter a height at all, in which case the program stops. 

# I used while loop, if statement, and try/except to do this.)


MINIMUM_HEIGHT: int = 50  # Minimum height requirement

def main():
    while True:
        height_input = input("How tall are you? (Press enter to exit) ")

        if height_input == "":
            print("Goodbye!")
            break  # stop the loop if the user pressed enter without input

        try:
            height = float(height_input)
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number.")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
