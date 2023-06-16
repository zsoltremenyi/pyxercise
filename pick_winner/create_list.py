
def creation():
    list_of_contestants = []
    while True:
        names = input("Enter a name: ")
        list_of_contestants.append(names)
        if not names:
            return list_of_contestants