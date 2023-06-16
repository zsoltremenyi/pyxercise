from random import choice
from create_list import creation


full_list = []
while True:

    list_of_contestants = creation()
    full_list.extend(list(filter(lambda x: x if x else None, list_of_contestants)))
    winner = choice(full_list)

    print(f"The winner is... {winner}")
    full_list.remove(winner)

    print(full_list)

    carry_on = input("Would you like to continue (y, n)? ")
    if carry_on == "n":
        break