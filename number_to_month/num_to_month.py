from translated_output import Translation


language_prompt = input("What language would you like to use? ")


try:
    translation = Translation(language_prompt)
except ValueError as err:
    print(str(err) + ", please input valid language.")
else:
    print(translation.trans_output(translation.trans_input()))