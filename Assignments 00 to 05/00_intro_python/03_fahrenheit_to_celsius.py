"""Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius."""

def main():
  print(f"Convert the Temperature from Fahrenheit to Celsius!:)")

  fahrenheit_input = input ("Enter temperture in fahrenheit: ")
  degrees_fahrenheit = float(fahrenheit_input)
  degrees_celsius = (degrees_fahrenheit - 32)*5.0/9.0

  print (f"Fahrenheit Temperature {fahrenheit_input} = {degrees_celsius}")

if __name__ == '__main__':
  main()