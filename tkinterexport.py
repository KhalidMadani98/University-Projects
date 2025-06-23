from tkinter import *
from tkinter import ttk
import csv

window = Tk()
window.title("Tkinter GUI")
window.geometry("400x400")

def save():
    peopleInfo = [a1.get(), b1.get(), clicked.get()]
    peopleInfoCSV = open("people_info.csv", "a+", newline="")
    writer = csv.writer(peopleInfoCSV)
    writer.writerow(peopleInfo)
    peopleInfoCSV.close()

a = Label(window ,text = "First Name").grid(row = 0,column = 0)
b = Label(window ,text = "Last Name").grid(row = 1,column = 0)
c = Label(window ,text = "Sex").grid(row = 2,column = 0)

a1 = Entry(window)
a1.grid(row = 0,column = 1)
b1 = Entry(window)
b1.grid(row = 1,column = 1)
clicked = StringVar(window)
c1 = OptionMenu(window, clicked,"Male", "Female", "Other").grid(row = 2,column = 1)

btn = ttk.Button(window ,text="Submit", command=save).grid(row=4,column=0)

window.mainloop()