from from_fahrenheit import Fahrenheit
from from_celsius import Celsius
from from_kelvin import Kelvin



flag = True
choices = ["c","f","k"]

while flag:
    choice_temp = input("Press C to convert from Celsius.\n"
                        "Press F to convert from Fahrenheit.\n"
                        "Press K to convert from Kelvin. \n")

    desired_temp = input("\nPress C to convert to Celsius.\n"
                         "Press F to convert from Fahrenheit.\n"
                         "Press K to convert from Kelvin. \n")


    if choice_temp.lower() == 'c' and desired_temp.lower() in choices:
        try:
            c = float(input("Please enter the temperature in celsius: \n"))
        except ValueError:
            print("Value error, invalid input")
        else:
            if desired_temp.lower() == 'f':
                print(Celsius(c).c_to_fh())
            elif desired_temp.lower() == 'k':
                print(Celsius(c).c_to_k())


    elif choice_temp.lower() == "f" and desired_temp.lower() in choices:
        try:
            f = float(input("Please enter the temperature in fahrenheit: "))
        except ValueError:
            print("Value error, invalid input")
        else:
            if desired_temp.lower() == "c":
                print(Fahrenheit(f).fh_to_c())
            elif desired_temp.lower() == "k":
                print(Fahrenheit(f).fh_to_k())


    elif choice_temp.lower() == "k" and desired_temp.lower() in choices:
        try:
            k = float(input("Please enter the temperature in kelvin: "))
        except ValueError:
            print("Value error, invalid input")
        else:
            if desired_temp.lower() == "c":
                print(Kelvin(k).kelv_to_celsius())
            elif desired_temp.lower() == "f":
                print(Kelvin(k).kelv_to_fahrenheit())

    else:
        print("Please enter valid input.")

    quitting = input("\nEnter Q to quit. \nIf you wish to carry on just press 'Enter'.\n")
    if quitting.lower() == 'q':
        flag = False