print("Welcome to the temperature converter!")
print("Options:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
option = int(input("Select one option: "))

if option == 1:
    Celsius = int(input("Enter the temperature in Celsius: "))
    Fahrenheit = (Celsius * 9/5) + 32
    print("The temperature in Fahrenheit is:", Fahrenheit)

elif option == 2:
    Fahrenheit = int(input("Enter the temperature in Fahrenheit: "))
    Celsius = Fahrenheit * 5/9 -32
    print("The temperature in Celsius is:", Celsius)

else:
    print("Select a valid option")
