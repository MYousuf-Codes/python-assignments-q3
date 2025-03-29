
# Simulate rolling two dice, and prints results of each roll as well as the total.

import random

NUM_SIDES : int = 6

def main():
  die1: int = random.randint(1, NUM_SIDES)
  die2: int = random.randint(1, NUM_SIDES)
  total : int = die1 + die2

  print(f"The Dice have the {NUM_SIDES} sides each :)")
  print(f"The First Die: {die1}")
  print(f"The Second Die: {die2}")
  print(f"The total of the Two Dice: {total}")

if __name__ == "__main__":
  main()