import dictionaries
from translate import Translator


month = dictionaries.month_dict
language = dictionaries.LANGUAGES


key_list = list(language.keys())
value_list = list(language.values())


language_prompt = input("What language would you like to use? ")
chosen_language = key_list[value_list.index(language_prompt)]


translator = Translator(to_lang=chosen_language)
translated_input = translator.translate('Please enter the number of the month: (1-12) ')
num = input(translated_input + " ")
translated_output = translator.translate(f'The name of the month is {month[num]}.')


print(translated_output)
