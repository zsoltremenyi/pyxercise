def first_name(fname):
    if len(fname) >= 2 and fname.isalpha():
        return fname
    else:
        return "First name must be at least two characters and shall only " \
               "contain letters."


print(first_name("4ff"))

