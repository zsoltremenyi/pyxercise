from random import choice


answers = ["Yes", "No", "Maybe", "Ask again later"]


while True:
    prompt = input("What's your question? ")
    print(choice(answers))
    more_questions = input("Do you have any more questions? (y, n) ")
    if more_questions == "n":
        break

