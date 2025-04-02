MARS_MULTIPLE = 0.378

def main():
    print("Welcome to the Mars Weight Calculator!")
    print("---------------------------------------")
    print("This program will calculate your weight on Mars.\n")
    
    earth_weight = float(input("Please enter your weight on Earth (in pounds): "))
    mars_weight = round(earth_weight * MARS_MULTIPLE, 2)
    
    print(f"Your weight on Mars is {mars_weight}")

if __name__ == "__main__":
    main()
