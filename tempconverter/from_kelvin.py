class Kelvin:
    def __init__(self, kelvin):
        self.kelvin = kelvin

    def kelv_to_celsius(self):
        celsius = self.kelvin - 273.15
        return celsius

    def kelv_to_fahrenheit(self):
        fahrenheit = (self.kelvin - 273.15)
        return fahrenheit