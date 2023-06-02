from calculator import calculateMonthsUntilPaidOff


balance = float(input("What is your balance? "))
card_apr = float(input("What is the APR on the card (as a percent)? "))
monthly_payment = float(input("What is the monthly payment you can make? "))


print(calculateMonthsUntilPaidOff(card_apr, balance, monthly_payment))
