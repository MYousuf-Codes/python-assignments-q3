
# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

import math  # importing math module to use math.sqrt()

def main():
    # Prompt the user to enter the lengths of sides AB and AC
    ab_input = input("Enter the length of AB: ")
    ac_input = input("Enter the length of AC: ")

    # Convert the inputs to float (to handle decimals)
    ab = float(ab_input)
    ac = float(ac_input)

    # Apply the Pythagorean theorem: BC^2 = AB^2 + AC^2
    bc_squared = ab ** 2 + ac ** 2
    bc = math.sqrt(bc_squared)  # Calculate the square root for hypotenuse

    # result
    print(f"The Result:")
    print(f"The length of BC (the hypotenuse) is: {round(bc, 2)}")

if __name__ == '__main__':
    main()