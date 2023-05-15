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
    cels_to_kelv = Celsius(c)
    print(cels_to_kelv.c_to_k())

elif choice_temp.lower() == "f" and desired_temp.lower() == "c":
    f = int(input("Please enter the temperature in fahrenheit: "))
    fahr_to_cels = Fahrenheit(f)
    print(fahr_to_cels.fh_to_c())

elif choice_temp.lower() == "f" and desired_temp.lower() == "k":
    f = int(input("Please enter the temperature in fahrenheit: "))
    fahr_to_k = Fahrenheit(f)
    print(fahr_to_k.fh_to_k())

elif choice_temp.lower() == "k" and desired_temp.lower() == "c":
    k = int(input("Please enter the temperature in kelvin: "))
    kel_to_cels = Kelvin(k)
    print(kel_to_cels.kelv_to_celsius())

elif choice_temp.lower() == "k" and desired_temp.lower() == "f":
    k = int(input("Please enter the temperature in kelvin: "))
    kel_to_cels = Kelvin(k)
    print(kel_to_cels.kelv_to_fahrenheit())