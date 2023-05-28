from translate import Translator
import dictionaries

month = dictionaries.month_dict
language = dictionaries.LANGUAGES


key_list = list(language.keys())
value_list = list(language.values())


class Translation():
    """
    A class that handles translation of month numbers to names in different languages.

    args:
        prompt (str): The language prompt provided by the user.

    attributes:
        prompt (str): The language prompt provided by the user.
        chosen_lang: The language code chosen based on the user prompt.
        translator (Translator): The translation object for the chosen language.
    """

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
            raise ValueError(f"{number} is not a valid number (1-12).") from ke
        else:
            return translated_output