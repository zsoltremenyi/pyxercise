import numpy as np
import math


def calculateMonthsUntilPaidOff(apr, balance, mpayment):
    apr = apr/100/365
    balance = round(balance, 2)
    mpayment = round(mpayment, 2)
    n = math.ceil(-1 / 30 * (np.log10(1 + balance / mpayment * (1 - (1 + apr) ** 30)) / np.log10(1 + apr)))
    print(n)
    return "It will take %g months to pay off this card." % n