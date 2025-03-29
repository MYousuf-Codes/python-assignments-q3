# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

def main():
    feet_input = input("Enter length in feet: ")
    feet = float(feet_input)
    inches = feet * 12

    # Handle singular/plural
    feet_unit = "foot" if feet == 1 else "feet"
    inch_unit = "inch" if inches == 1 else "inches"

    print(f"{feet} {feet_unit} is equal to {inches} {inch_unit}.")

if __name__ == '__main__':
    main()
