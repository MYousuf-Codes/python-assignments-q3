# Fill out the function get_last_element(lst) which takes in a list lst
#  as a parameter and prints the last element in the list. 
# The list is guaranteed to be non-empty, but there are no guarantees on its length.



def get_first_element(lst):

    print(lst[-1])
    # print(lst[len(lst) - 1])

def get_lst():
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)


if __name__ == '__main__':
    main()