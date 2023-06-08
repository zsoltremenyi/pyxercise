import re


class Employee:
    def __init__(self, id, zipc, fname, lname):
        self.id = id
        self.zipc = zipc
        self.fname = fname
        self.lname = lname

    def employee_id(self):
        if len(self.id) == 7:
            if re.match("^[a-zA-Z]+$", self.id[:2]) and re.match("-", self.id[2]) and re.match("^[0-9]+$", self.id[3:]):
                return True
            else:
                print(f"Invalid ID: {self.id}\n"
                      f"A valid ID has the format: AA-1234\nPlease check.")
                return False
        print("Check length of ID.")
        return False

    def zipcode(self):
        if re.match("^[0-9]+$", self.zipc):
            return True
        print("Zipcodes may only contain numbers.")
        return False

    def first_name(self):
        if len(self.fname) >= 2 and re.match("^[a-zA-z]+$", self.fname):
            return True
        else:
            print("First names must contain only letters and length must be at least 2 characters.")
            return False

    def last_name(self):
        if len(self.lname) >= 2 and re.match("^[a-zA-z]+$", self.lname):
            return True
        else:
            print("Last name must be at least two characters and shall only " \
                  "contain letters.")
            return False