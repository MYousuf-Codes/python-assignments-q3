"""Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

✅ Prompt the user to enter the first number.

✅ Read the input and convert it to an integer.

✅ Prompt the user to enter the second number.

✅ Read the input and convert it to an integer.

✅ Calculate the sum of the two numbers.

✅ Print the total sum with an appropriate message.

The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum."""

def main():
    print("Add Two Numbers :)")

    num1: str = input("Enter first number: ")
    num1: int = int(num1)

    num2: str = input("Enter second number: ")
    num2: int = int(num2)

    sum_result: int = num1 + num2

    print(f"The sum of {num1} and {num2} is = {sum_result}")

if __name__ == '__main__':
    main()
