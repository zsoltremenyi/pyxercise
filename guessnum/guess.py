from random import randint
from guessing_module import guessing
from quitting import quitting

while True:
    difficulty = input("Pick a difficulty level (1, 2, or 3): ")

    hard = randint(1, 1000)
    if difficulty == "1":
        easy = randint(1, 10)
        prompt = input("I have my number. What's your guess? ")
        guessing(easy, prompt)
        if not quitting():
            break
    elif difficulty == "2":
        medium = randint(1, 100)
        prompt = input("I have my number. What's your guess? ")
        guessing(medium, prompt)
        if not quitting():
            break
    elif difficulty == "3":
        hard = randint(1, 1000)
        prompt = input("I have my number. What's your guess? ")
        guessing(hard,prompt)
        if not quitting():
            break
    else:
        print(f"{difficulty} is not a valid difficulty level. Please try again!")

