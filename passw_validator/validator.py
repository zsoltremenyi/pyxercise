login = {"dirk": "abc123"}

password = input("What is the password? ")

if password == login["dirk"]:
    print("Welcome!")
else:
    print("I don't know you.")