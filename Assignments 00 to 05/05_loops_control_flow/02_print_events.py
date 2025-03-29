# Write a program that prints the first 20 even numbers. There are several correct approaches, 
# but they all use a loop of some sort. Do no write twenty print statements


def main():
    # This for-loop start at 0 and counts up to 19 (for a total of 20 numbers)
    for even_numbers in range(20):
        print(even_numbers * 2)  # Use the 'even_numbers' value inside the for-loop
   
if __name__ == "__main__":
    main()