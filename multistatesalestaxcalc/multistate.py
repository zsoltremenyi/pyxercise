from statenameapi import State
from calculator import Calculator
import states


print(states.state_and_tax)
try:
    order_amount = float(input("What is the order amount? "))
    state = input("What state do you live in? (full name or postal abbriviation) ").title()


except:
    print("Invalid input, please try again.")


else:
    state_finder = State(state.upper())

    if state_finder.full_name():
        calc = Calculator(order_amount, state_finder.full_name())
        print(f"The tax is ${calc.tax_amount()}.\nThe total is ${calc.calculator()}.")

    elif state in states.state_and_tax.keys():
        calc = Calculator(order_amount, state)
        print(f"The tax is ${calc.tax_amount()}.\nThe total is ${calc.calculator()}.")

    else:
        print("Check input: only full name of state or postal abbriviation")
