from random import shuffle


choices = []


def pass_choice(passw):
    print("Password choices:")
    for _ in range(3):
        pass_string = "".join(passw)
        print(pass_string)
        choices.append(pass_string)
        shuffle(passw)