def last_name(lname):
    if len(lname) >= 2 and lname.isalpha():
        return lname
    else:
        return "Last name must be at least two characters and shall only " \
               "contain letters."