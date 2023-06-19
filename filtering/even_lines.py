with open(r".\justAtext.txt") as file:
    line_list = (x.strip() for x in file.readlines())
    for i, v in enumerate(line_list):
        if i % 2 != 0:
            print(v)
