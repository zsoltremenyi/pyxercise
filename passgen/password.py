import string
letter_list = list(string.ascii_letters)
spec_list = list(string.punctuation)
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(spec_list)

min_length = int(input("What's the minimum length? "))
spec_ch = int(input("How many special characters? "))
nums = int(input("How many numbers? "))
