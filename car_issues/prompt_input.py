def prompt_input(prompt):
    while True:
        value = input(prompt.lower())
        if value == 'y' or value == 'n':
            return value
        else:
            print("Please enter 'y' or 'n'. ")