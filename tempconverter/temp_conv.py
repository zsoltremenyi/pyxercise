from from_fahrenheit import fh_to_c
from from_celsius import c_to_fh

choice_temp = input("Press C to convert from Fahrenheit to Celsius.\n"
                    "Press F to convert from Celsius to Fahrenheit.\n"
                    "Press K to convert from Kelvin.")

if choice_temp.lower() == "c":
    fh = int(input("Please enter the temperature in Fahrenheit: "))
    print(fh_to_c(fh))
elif choice_temp.lower() == "f":
    c = int(input("Please enter the temperature in Fahrenheit: "))
    print(c_to_fh(c))

