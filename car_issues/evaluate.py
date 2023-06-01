from prompt_input import prompt_input


def evaluate():
    print('Please press "y" or "n" for answers.')

    prompt1 = prompt_input("Is the car silent when you turn the key? ")

    if prompt1 == 'y':
        prompt2 = prompt_input("Are the battery terminals corroded? ")
        if prompt2 == 'y':
            print("Clean terminals and try starting again.")
        elif prompt2 == 'n':
            print("Replace cables and try again.")
    elif prompt1 == 'n':
        prompt3 = prompt_input("Does the car make a clicking noise? ")
        if prompt3 == 'y':
            print("Replace the battery.")
        elif prompt3 == 'n':
            prompt4 = prompt_input("Does the car crank up but fail to start? ")
            if prompt4 == 'y':
                print("Check spark plug connections.")
            elif prompt4 == 'n':
                prompt5 = prompt_input("Does the engine start and then die? ")
                if prompt5 == 'y':
                    prompt6 = prompt_input("Does your car have fuel injection? ")
                    if prompt6 == 'y':
                        print("Get it in for service")
                    elif prompt6 == 'n':
                        print("Check to ensure the choke is opening and closing.")