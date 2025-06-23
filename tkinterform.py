from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Tkinter GUI")
window.geometry("400x400")

a = Label(window ,text = "First Name").grid(row = 0,column = 0)
b = Label(window ,text = "Last Name").grid(row = 1,column = 0)
c = Label(window ,text = "Sex").grid(row = 2,column = 0)

a1 = Entry(window).grid(row = 0,column = 1)
b1 = Entry(window).grid(row = 1,column = 1)
c1 = OptionMenu(window, StringVar(window),"Male", "Female", "Other").grid(row = 2,column = 1)
btn = ttk.Button(window ,text="Submit").grid(row=4,column=0)

window.mainloop()