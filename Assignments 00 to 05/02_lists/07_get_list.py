# Write a program which continuously asks the user to 
# enter values which are added one by one into a list. 
# When the user presses enter without typing anything, print the list.


def main():
    lst = []  # this is an empty list to store things in

    val = input("Enter a value: ")  # get an initial value
    while val:  # the user input isn't an empty value
        lst.append(val) # Add val to list
        val = input("Enter a value: ")  # the next value to add

    print("Here's the list:", lst)
    # Print the list after the user has finished entering values
if __name__ == '__main__':
    main()