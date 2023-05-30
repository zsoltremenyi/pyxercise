from largestnum import largest_num


num_set = set()
flag = True

while flag:
    something = input("Enter a number, when done enter 'q': ")
    if something == 'q':
        flag = False
    else:
        num_set.add(something)


print(largest_num(num_set))
