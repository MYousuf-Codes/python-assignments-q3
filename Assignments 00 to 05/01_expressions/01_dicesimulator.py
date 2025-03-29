
"""Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works."""

import random

NUM_SIDES : int = 6 # defined outside of any funciton, so it is accessible from anywhere and this is Global Scope


def roll_dice():

  die1 : int = random.randint(1, NUM_SIDES) # random.randint(1, NUM_SIDES) generates a random integer between 1 and 6.
  die2 : int = random.randint(1, NUM_SIDES) # same as above

  total : int = die1 + die2
  print(f"The total of tow dice = ", total)

  # Even though there is a variable named die1 in main() (coming up), this die1 is completely separate because it's inside a different function.
  #Local scope means variables exist only inside the function where they are defined.


def main():
  print(f"This program simulates rolling two dice, to show how variable scope works :)")

  die1: int = 10
  print("die1 in main() starts as: " + str(die1))
  roll_dice()
  roll_dice()
  roll_dice()
  print(f"die1 in main() is: "+ str(die1))

  # The die1 here in main() is not affected by the die1 inside roll_dice().
  # Even though they have the same name, they are in different scopes.

  # Variable scope means variables in different functions do not interfere, even with the same name.


if __name__ == "__main__":
  main()