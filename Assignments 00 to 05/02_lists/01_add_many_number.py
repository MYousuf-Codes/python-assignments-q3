
# Write a function that takes a list of numbers and returns the sum of those numbers.

def add_list_number (numbers)->int:
    total_so_far =0

    for number in numbers:
      total_so_far += number

    return total_so_far

def main():

    print("The sum of the Numbers, from a List :)")

    numbers : list[int] = [1,2,3,5,6,7,8,9,10]
    sum_of_numbers : int = add_list_number(numbers)
    print(sum_of_numbers)

if __name__ == "__main__":
    main()