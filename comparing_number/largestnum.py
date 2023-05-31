def largest_num(numbers):
    max_num = 0
    for i in numbers:
        if not max_num:
            max_num = i
        elif max_num < i:
            max_num = i
    return max_num

print(largest_num([-1, g, -19]))