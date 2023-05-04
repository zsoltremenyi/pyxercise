from tkinter import *
from tkinter import ttk
from git_project.pyxercise.compound.calculation import compound_interest

root = Tk()
root.geometry("400x350")
frame = ttk.Frame(root, padding=10)
frame.grid()
title = ttk.Label(frame, text="Determining Compound Interest")
title.grid(row=0, column=0, columnspan=2, padx=100, pady=20)


ttk.Label(frame, text='amount').grid(column=0, row=1, pady=10, padx=10)
amount = Entry(frame, width=20)
amount.grid(column=1, row=1)

ttk.Label(frame, text='rate').grid(column=0, row=2, pady=10, padx=10)
rate = Entry(frame, width=20)
rate.grid(column=1, row=2)

ttk.Label(frame, text='years').grid(column=0, row=3, pady=10, padx=10)
years = Entry(frame, width=20)
years.grid(column=1, row=3)

ttk.Label(frame, text='compound per year').grid(column=0, row=4, pady=10, padx=10)
cpy = Entry(frame, width=20)
cpy.grid(column=1, row=4)


sumup = Entry(frame, width=20)
sumup.grid(column=0, row=6, columnspan=2)


quitting = ttk.Button(frame, text="Quit", command=root.destroy)
quitting.grid(column=1, row=7, pady=10)


calculate = ttk.Button(frame, text="Calculate", command=lambda: [sumup.delete(0, END), sumup.insert(0, compound_interest(amount.get(),rate.get(),years.get(),cpy.get()))])
calculate.grid(column=0, row=7, pady=10)


reset = ttk.Button(frame, text="Reset", command=lambda: [sumup.delete(0, END), amount.delete(0, END), rate.delete(0, END), years.delete(0, END), cpy.delete(0, END)])
reset.grid(column=0, row=8, columnspan=2)


root.mainloop()