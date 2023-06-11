def guessing(difficulty, prompt):
    counter = 0
    while True:
        if str(difficulty) == str(prompt):
            counter += 1
            print(f"You got it in {counter} guesses!")
            return
        elif str(difficulty) > str(prompt):
            counter += 1
            prompt = input("Too low guess again: ")
        elif str(difficulty) < str(prompt):
            counter += 1
            prompt = input("Too high guess again: ")