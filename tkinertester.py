from tkinter import *

window = Tk()
window.title('Tkinter GUI')
window.geometry('400x400')

label = Label(window, text='Hello World!').pack()
button = Button(window, text='click here to close program', width=25, command=window.destroy)
button.pack()

window.mainloop()