from tkinter import *
from tkinter import ttk
import csv

window = Tk()
window.title("Tkinter GUI")

tree = ttk.Treeview(window, column=("First Name", "Last Name", "Sex"), show="headings")
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="First Name")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Last Name")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Sex")

csvData = csv.reader(open("people.csv", "r+"))
listOfPeople = list(csvData)

for person in listOfPeople:
    tree.insert(parent="",index="end", text="1", values=(person[0], person[1], person[2]))
tree.pack()

window.mainloop()