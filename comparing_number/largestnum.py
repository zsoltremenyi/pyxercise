def largest_num(numbers):
    """returns the largest number in list"""

    max_num = 0

    for i in numbers:
        if not max_num:
            max_num = i
        elif max_num < i:
            max_num = i
    return max_num