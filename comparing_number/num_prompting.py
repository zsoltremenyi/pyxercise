def prompting():
    flag = True
    num_set = set()
    while flag:
        try:
            something = int(input("Enter a number: "))
            exiting = input("If done, press 'q', else press 'enter': ")
        except ValueError as ve:
            raise ValueError(f"{ve} not valid, please enter a valid number")
        else:
            if exiting == 'q':
                num_set.add(something)
                flag = False
            elif exiting == '':
                num_set.add(something)
            elif exiting.isalnum() or not exiting.isalnum():
                print(f"'{exiting}' Wrong character, prompting for next number.")
        set_without_brackets = [str(i) for i in num_set]
        print(f"Current number(s): {', '.join(set_without_brackets)}")

    return num_set