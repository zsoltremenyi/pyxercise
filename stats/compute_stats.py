from calculations import Calculations


num_list = []
while True:
    number = input("Enter a number:\nIf done, enter 'done'\n ")
    if number == 'done':
        calc = Calculations(num_list)
        print("Numbers: " + ", ".join(list(map(lambda x: str(x), num_list))))
        print(f"The average is {calc.mean()}.\n"
              f"The minimum is {min(num_list)}.\n"
              f"The maximum is {max(num_list)}.\n"
              f"The standard deviation is {calc.standard_dev()}.")
        break
    elif number.isdigit():
        num_list.append(float(number))
    else:
        print("Invalid input.")





