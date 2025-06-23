from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Tkinter GUI")

tree = ttk.Treeview(window, column=("First Name", "Last Name", "Sex"), show="headings")
tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="First Name")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Last Name")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Sex")

tree.insert(parent="",index="end", text="1", values=("Ste", "Bigoude", "Male"))
tree.insert(parent="",index="end", text="1", values=("Tammy", "Abdullah", "Female"))
tree.insert(parent="",index="end", text="1", values=("Adam", "Mitchell", "Male"))
tree.insert(parent="",index="end", text="1", values=("Leyla", "Yaltiligil", "Female"))
tree.insert(parent="",index="end", text="1", values=("Dani", "Ivory", "Other"))
tree.pack()

window.mainloop()