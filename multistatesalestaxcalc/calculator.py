import states


class Calculator:
    salestax_dict = states.state_and_tax

    def __init__(self, amount, state):
        self.amount = amount
        self.state = state
        self.tax = float(self.salestax_dict[self.state]) / 100


    def tax_amount(self):
        #tax = float(self.salestax_dict[self.state]) / 100
        tax_amount = self.amount*self.tax
        return tax_amount

    def calculator(self):
        #tax = float(self.salestax_dict[self.state]) / 100
        return round(self.amount*(1+self.tax), 2)
