from largestnum import largest_num


num_set = set()
flag = True

while flag:
    try:
        something = int(input("Enter a number: "))
        exiting = input("If done, press 'q', else press 'enter': ")
    except ValueError as ve:
        raise ValueError(f"{ve} not valid, please enter a valid number")
    else:
        if exiting == 'q':
            flag = False
        else:
            num_set.add(something)


print(largest_num(num_set))
