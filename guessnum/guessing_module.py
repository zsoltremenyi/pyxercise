def guessing(difficulty, prompt):
    counter = 0
    num_list = []
    while True:

        if str(difficulty) == str(prompt):
            counter += 1
            print(f"You got it in {counter} guesses!")
            return

        elif str(difficulty) > str(prompt):
            if prompt in num_list:
                print(f"Already guessed {prompt}.")
            elif prompt not in num_list:
                num_list.append(prompt)
            counter += 1
            prompt = input("Too low guess again: ")

        elif str(difficulty) < str(prompt):
            if prompt in num_list:
                print(f"Already guessed {prompt}.")
            elif prompt not in num_list:
                num_list.append(prompt)
            counter += 1
            prompt = input("Too high guess again: ")

