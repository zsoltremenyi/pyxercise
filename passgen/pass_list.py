from random import randint, choice, shuffle


your_pass = []


class PasswordComp:
    def __init__(self, letters, numbers, characters):
        self.letters = letters
        self.numbers = numbers
        self.characters = characters

    def specials(self):
        return your_pass.append(choice(self.characters))

    def number_choice(self):
        return your_pass.append(str(choice(self.numbers)))

    def letter(self):
        return your_pass.append(choice(self.letters))

