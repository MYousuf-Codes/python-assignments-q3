
# Ask the user for a number and print its square (the product of the number times itself).

def main():
  print("The Square of the User Input :)")

  number_input : float = float(input("Enter the number to see its square: "))
  print(str (number_input)+ " squared is: " + (str (number_input * number_input)))

if __name__ == '__main__':
  main()