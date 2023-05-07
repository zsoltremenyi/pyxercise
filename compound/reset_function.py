from tkinter import *
from tkinter import ttk

def del_func(val1, val2, val3, val4, val5):
    return val1.delete(0, END), val2.delete(0, END), val3.delete(0, END), val4.delete(0, END), val5.delete(0, END)

def insert_func(val1, val2, val3, val4, val5):
    return val1.insert(0, 0), val2.insert(0, 0), val3.insert(0, 0), val4.insert(0, 0), val5.insert(0, 0)