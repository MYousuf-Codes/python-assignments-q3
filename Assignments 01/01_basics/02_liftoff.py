# Write a program that prints out the calls for a spaceship that is about to launch. 
# Countdown from 10 to 1 and then output Liftoff!

def main():
    """
    Prints a countdown from 10 to 1, followed by 'Liftoff!'.
    """
    for i in range(10, 0, -1):  # Start at 10, go down to 1
        print(i, end=" ")  # Print numbers on the same line

    print("Liftoff!")  # Print "Liftoff!" at the end

if __name__ == '__main__':
    main()
