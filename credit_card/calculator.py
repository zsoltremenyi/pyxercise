import numpy as np
import math


def calculateMonthsUntilPaidOff(apr, balance, mpayment):
    apr = apr / 100 / 365
    balance = round(balance, 2)
    mpayment = round(mpayment, 2)
    n = math.ceil(-1 / 30 * (np.log10(1 + balance / mpayment * (1 - (1 + apr) ** 30)) / np.log10(1 + apr)))

    return "It will take %g month(s) to pay off this card." % n


def calculatePaymentForDesireMonth(apr, balance, month):
    apr = apr / 100 / 365
    balance = round(balance, 2)
    mpayment = math.ceil(balance * (1 - (1 + apr) ** 30) / (10 ** ((month * 30 * np.log10(1 + apr)) / -1) - 1))

    return "You have to pay $%g to pay off this card in %g month(s)" % (mpayment, month)
