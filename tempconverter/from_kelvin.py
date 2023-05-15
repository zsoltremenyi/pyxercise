class Kelvin:
    def __init__(self, kelvin):
        self.kelvin = kelvin

    def kelv_to_celsius(self):
        celsius = self.kelvin - 273.15
        return f"{self.kelvin} Kelvin is {celsius} Celsius."

    def kelv_to_fahrenheit(self):
        fahrenheit = ((self.kelvin - 273.15) * 9 / 5) + 32
        return f"{self.kelvin} Kelvin is {round(fahrenheit, 2)} Fahrenheit."