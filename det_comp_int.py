import math

try:
    principal_amount = float(input("What is the principal amount? "))
    an_rate = float(input("What is the rate? "))
    num_years = int(input("What is the number of years? "))
    compound = int(input("What is the number of times the interest is compounded per year? "))


    def compound_interest(amount, rate, years, comperyear):
        rate = rate / 100
        end_of_investment = round(amount * math.pow((1 + rate / comperyear), comperyear * years), 2)
        return f"${amount} invested at {rate * 100}% for {years} years compounded {compound}" \
               f" times per year is ${end_of_investment}."

except ValueError:
    print("Please enter valid value")

else:
    print(compound_interest(principal_amount,an_rate,num_years,compound))