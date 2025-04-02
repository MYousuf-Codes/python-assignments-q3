# Problem 1 List
def list_practice():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    print("Initial list length:", len(fruit_list))
    
    fruit_list.append('mango')
    
    print("Updated fruit list:", fruit_list)



# Problem 2 Index Game


def access_element(lst, index):
    """Return the element at the specified index or an error message if out of range."""
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    """Replace the element at the specified index with the new value or return an error message."""
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    """Return a slice of the list from start index up to (but not including) the end index."""
   
    return lst[start:end]

def index_game():
    """A text-based game to access, modify, or slice a list."""
    lst = [1, 2, 3, 4, 5]  # list
    print("Current list:", lst)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ").strip().lower()

    if operation == "access":
        try:
            index = int(input("Enter index to access: "))
            result = access_element(lst, index)
            print("Element at index", index, ":", result)
        except ValueError:
            print("Invalid input. Please enter a valid integer for the index.")
    elif operation == "modify":
        try:
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            result = modify_element(lst, index, new_value)
            print("Updated list:", result)
        except ValueError:
            print("Invalid input. Please enter a valid integer for the index.")
    elif operation == "slice":
        try:
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(lst, start, end)
            print("Sliced list:", result)
        except ValueError:
            print("Invalid input. Please enter valid integers for the indices.")
    else:
        print("Invalid operation.")


def main():
    print("Select the problem to run:")
    print("1. List Practice")
    print("2. Index Game")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        print("\n--- Running List Practice ---")
        list_practice()
    elif choice == "2":
        print("\n--- Running Index Game ---")
        index_game()
    else:
        print("Invalid choice. Please run the program again and choose 1 or 2.")

if __name__ == "__main__":
    main()


# EXAMPLE run: for access

"""
Select the problem to run:
1. List Practice
2. Index Game
Enter 1 or 2: 2

--- Running Index Game ---
Current list: [1, 2, 3, 4, 5]
Choose an operation: access, modify, slice
Enter operation: access
Enter index to access: 1
Element at index 1 : 2

"""