first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))

num_list = [first, second, third]
largest_num = 0

for i in num_list:
    if not largest_num:
        largest_list = i
    elif largest_num < int(i):
        largest_num = int(i)

print(largest_num)

