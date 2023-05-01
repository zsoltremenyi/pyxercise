import math
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("400x350")
frame = ttk.Frame(root, padding=10)
frame.grid()
title = ttk.Label(frame, text="Determining Compound Interest")
title.grid(row=0, column=0, columnspan=2, padx=100, pady=20)


quit = ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=6, pady=10)
calculate = ttk.Button(frame, text="Calculate", command="").grid(column=0, row=6, pady=10)

ttk.Label(frame, text='amount').grid(column=0, row=1, pady=10, padx=10)
amount = Entry(frame, width=20)
#amount.insert(0, int(input()))
amount.grid(column=1, row=1)

ttk.Label(frame, text='rate').grid(column=0, row=2, pady=10, padx=10)
rate = Entry(frame, width=20)
#rate.insert(0, 'rate')
rate.grid(column=1, row=2)

ttk.Label(frame, text='years').grid(column=0, row=3, pady=10, padx=10)
rate = Entry(frame, width=20)
#rate.insert(0, 'rate')
rate.grid(column=1, row=3)

ttk.Label(frame, text='compound per year').grid(column=0, row=4, pady=10, padx=10)
rate = Entry(frame, width=20)
#rate.insert(0, 'rate')
rate.grid(column=1, row=4)

root.mainloop()

# def compound_interest(amount, rate, years, comperyear):
#     rate = rate / 100
#     end_of_investment = round(amount * math.pow((1 + rate / comperyear), comperyear * years), 2)
#     return f"${amount} invested at {rate * 100}% for {years} years compounded {compound}" \
#            f" times per year is ${end_of_investment}."
#
# try:
#     principal_amount = float(input("What is the principal amount? "))
#     an_rate = float(input("What is the rate? "))
#     num_years = int(input("What is the number of years? "))
#     compound = int(input("What is the number of times the interest is compounded per year? "))
#
#
# except ValueError:
#     print("Please enter valid value")
#
# else:
#     print(compound_interest(principal_amount,an_rate,num_years,compound))