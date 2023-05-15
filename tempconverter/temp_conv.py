from from_fahrenheit import Fahrenheit
from from_celsius import Celsius
from from_kelvin import Kelvin

choice_temp = input("Press C to convert from Celsius.\n"
                    "Press F to convert from Fahrenheit.\n"
                    "Press K to convert from Kelvin. ")

desired_temp = input("Press C to convert to Celsius.\n"
                     "Press F to convert from Fahrenheit.\n"
                     "Press K to convert from Kelvin. ")

if choice_temp.lower() == "c" and desired_temp.lower() == "f":
    c = int(input("Please enter the temperature in celsius: "))
    cels_to_fahr = Celsius(c)
    print(cels_to_fahr.c_to_fh())

elif choice_temp.lower() == "c" and desired_temp.lower() == "k":
    c = int(input("Please enter the temperature in celsius: "))
    cels_to_fahr = Celsius(c)
    print(cels_to_fahr.c_to_k())

