# Write a program that reads a year from the user and tells whether a given year is a leap year or not.

def main():
    # Get the year to check from the user
    year = int(input("Please input a year: "))

    # Checking leap year conditions
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("That's a leap year!")
            else:
                print("That's not a leap year.")
        else:
            print("That's a leap year!")
    else:
        print("That's not a leap year.")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
