import states


class Calculator:
    salestax_dict = states.state_and_tax

    def __init__(self, amount, state):
        self.amount = amount
        self.state = state

    def calculator(self):
        tax = float(self.salestax_dict[self.state])
        return round(self.amount*(1+tax/100), 2)
