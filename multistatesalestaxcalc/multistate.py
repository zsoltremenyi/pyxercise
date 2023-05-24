from statenameapi import State
from calculator import Calculator
import states

order_amount = float(input("What is the order amount? "))
state = input("What state do you live in? (full name or postal abbriviation) ").title()


state_finder = State(state.upper())



if state_finder.full_name():
    calc = Calculator(order_amount, state_finder.full_name())
    print(calc.calculator())
elif state in states.state_and_tax:
    calc = Calculator(order_amount, state)
    print(calc.calculator())




# print(state_finder.full_name())

