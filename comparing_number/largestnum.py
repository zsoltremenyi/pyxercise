def largest_num(numbers):
    max_num = 0
    for i in numbers:
        if not largest_num:
            largest_list = i
        elif max_num < int(i):
            max_num = int(i)