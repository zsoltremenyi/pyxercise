class Fahrenheit:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    def fh_to_c(self):
        celsius = (self.fahrenheit-32) * 5/9
        return f"{self.fahrenheit} Fahrenhiet is {celsius} Celsius."

    def fh_to_k(self):
        kelvin = (self.fahrenheit-32) * 5/9 + 273.15
        return f"{self.fahrenheit} Fahrenhiet is {round(kelvin, 2)} Kelvin."