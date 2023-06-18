from random import randint, choice, shuffle


your_pass = []


class PasswordComp:
    def __init__(self, letters, numbers, characters, spec_ch, nums):
        self.letters = letters
        self.numbers = numbers
        self.characters = characters
        self.spec_ch = spec_ch
        self.nums = nums

    def specials(self):
        return your_pass.append(choice(self.characters))

    def number_choice(self):
        return your_pass.append(str(choice(self.numbers)))

    def letter(self):
        return your_pass.append(choice(self.letters))

