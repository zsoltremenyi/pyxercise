from check_int import check_integer

prompted_nums = input("Enter a list of numbers, separated by spaces: ")
list_of_nums = prompted_nums.split()
check_if_num = filter(lambda x: check_integer(x), list_of_nums)


even_nums = filter(lambda x: int(x) % 2 == 0, check_if_num)

if even_nums == True:
    print(f"The even numbers are {' '.join(even_nums)}.")
else:
    print(f"There are no even nums.")


