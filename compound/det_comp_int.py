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
#amount.insert(0, int(input()))
amount.grid(column=1, row=1)

ttk.Label(frame, text='rate').grid(column=0, row=2, pady=10, padx=10)
rate = Entry(frame, width=20)
#rate.insert(0, 'rate')
rate.grid(column=1, row=2)

ttk.Label(frame, text='years').grid(column=0, row=3, pady=10, padx=10)
years = Entry(frame, width=20)
#rate.insert(0, 'rate')
years.grid(column=1, row=3)

ttk.Label(frame, text='compound per year').grid(column=0, row=4, pady=10, padx=10)
cpy = Entry(frame, width=20)
#rate.insert(0, 'rate')
cpy.grid(column=1, row=4)


sumup = Entry(frame, width=20)
sumup.grid(column=0, row=6, columnspan=2)

ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=7, pady=10)


ttk.Button(frame, text="Calculate", command=lambda: [sumup.delete(0, END), sumup.insert(0, compound_interest(amount.get(),rate.get(),years.get(),cpy.get()))]).grid(column=0, row=7, pady=10)




root.mainloop()

