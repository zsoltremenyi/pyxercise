import pyperclip


def copying_pass(list_of_passwords):
    choosing_pass = input("Which one do you prefer? (1,2,3) \n"
                          "Your choice will be copied to clipboard.\n")

    if choosing_pass == "1":
        return pyperclip.copy(list_of_passwords[0])
    elif choosing_pass == "2":
        return pyperclip.copy(list_of_passwords[1])
    elif choosing_pass == "3":
        return pyperclip.copy(list_of_passwords[2])
    else:
        return "Invalid input"