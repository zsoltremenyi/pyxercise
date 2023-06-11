def guessing(difficulty, prompt):
    counter = 0
    while True:
        if difficulty == int(prompt):
            counter += 1
            print(f"You got it in {counter} guesses!")
            return
        elif difficulty > int(prompt):
            counter += 1
            prompt = input("Too low guess again: ")
        elif difficulty < int(prompt):
            counter += 1
            prompt = input("Too high guess again: ")