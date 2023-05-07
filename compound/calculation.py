import math


def compound_interest(amount, rate, years, comperyear):
    try:
        rate = float(rate) / 100
        end_of_investment = round(
            float(amount) * math.pow((1 + float(rate) / float(comperyear)), float(comperyear) * float(years)), 2)
    except:
        return "Invalid input."
    else:
        print(f"${amount} invested at {rate * 100}% for {years} years compounded {comperyear}"\
              f" times per year is ${end_of_investment}.")
        return str(end_of_investment)


