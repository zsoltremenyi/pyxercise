from calculator import calculateMonthsUntilPaidOff
from calculator import calculatePaymentForDesireMonth
import prompts


print("Would you like to provide the number of months until pay off, or the amount you would like to pay per month?")
choosing_option = input("Press 'm' for month, 'a' for monthly amount. ")


if choosing_option == 'a':
    try:
        month_till_payoff = calculateMonthsUntilPaidOff(prompts.card_apr(), prompts.balance(), prompts.monthly_payment())
    except ValueError:
        raise "Invalid input"
    else:
        print(month_till_payoff)
elif choosing_option == 'm':
    try:
        amount_to_pay_monthly = calculatePaymentForDesireMonth(prompts.card_apr(),prompts.balance(), prompts.month())
    except ValueError:
        raise "invalid input"
    else:
        print(amount_to_pay_monthly)
else:
    print("Invalid input.")