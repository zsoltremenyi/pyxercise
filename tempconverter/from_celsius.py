class Celsius:
    def __init__(self, celsius):
        self.celsius = celsius

    def c_to_fh(self):
        fahrenheit = (self.celsius * 9 / 5) + 32
        return f"{self.celsius} Celsius is {fahrenheit} Fahrenheit."

    def c_to_k(self):
        kelvin = self.celsius + 273.15
        return f"{self.celsius} Celsius is {kelvin} Kelvin."