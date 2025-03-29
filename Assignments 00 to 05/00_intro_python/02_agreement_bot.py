
"""Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course)."""

def main():
    print("Agreement Bot :)")

    favourite_animal : str = input("What's your Favourite Animal? ")
    print(f"My Favourite Animal is {favourite_animal}!")


if __name__ == '__main__':
    main()