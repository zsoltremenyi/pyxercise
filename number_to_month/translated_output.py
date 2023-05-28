from translate import Translator
import dictionaries

month = dictionaries.month_dict
language = dictionaries.LANGUAGES


key_list = list(language.keys())
value_list = list(language.values())


class Translation():
    def __init__(self,prompt):
        self.prompt = prompt
        self.chosen_lang = key_list[value_list.index(prompt)]
        self.translator = Translator(to_lang=self.chosen_lang)

    def trans_input(self):
        translated_input = self.translator.translate('Please enter the number of the month: (1-12) ')
        num = input(translated_input + " ")
        return num

    def trans_output(self, number):
        try:
            translated_output = self.translator.translate(f'The name of the month is {month[number]}.')
        except KeyError as ke:
            return self.translator.translate("KeyError: " + str(ke) + " is not a valid number (1-12). ")
        else:
            return translated_output