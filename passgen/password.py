import random
import string
import pass_list as pl
import pass_choices as pc
from copy_password import copying_pass

letter_list = list(string.ascii_letters)
spec_list = list(string.punctuation)
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


try:
    min_length = int(input("What's the minimum length? "))
    spec_ch = int(input("How many special characters? "))
    nums = int(input("How many numbers? "))

except ValueError:
    raise ValueError

else:
    pass_comp = pl.PasswordComp(letter_list, num_list, spec_list, spec_ch, nums)
    while min_length > 0:
        for _ in range(spec_ch):
            pass_comp.specials()
            min_length -= 1
        for _ in range(nums):
            pass_comp.number_choice()
            min_length -= 1
        if min_length <= 0:
            letter_length = random.randint(1,4)
            for _ in range(letter_length):
                pass_comp.letter()
        elif min_length > 0:
            letter_length = random.randint(0,4)
            for _ in range(min_length+letter_length):
                pass_comp.letter()
                min_length -= 1

password = pl.your_pass
pc.pass_choice(password)
pass_list = pc.choices
copying_pass(pass_list)