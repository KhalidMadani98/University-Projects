import tkinter as tk
from tkinter import ttk, VERTICAL, RIGHT, Y, HORIZONTAL, BOTTOM, X, filedialog, messagebox, LEFT, END
from tkinter.filedialog import asksaveasfile

import pandas as pd


#Defining class
class EmployeeManagementGUI(tk.Tk):
#This function uses self to define the class
    def __init__(self):
        super().__init__()

#a list of variables which are defined
        self.employeeID = tk.StringVar()
        self.firstname = tk.StringVar()
        self.lastname = tk.StringVar()
        self.gender = tk.StringVar()
        self.email = tk.StringVar()
        self.contactnumber = tk.StringVar()
        self.Role = tk.StringVar()
        self.salary = tk.StringVar()
        self.country = tk.StringVar()
        self.EmergencyContact = tk.StringVar()
        self.shift = tk.StringVar()
        self.DOB = tk.StringVar()
        self.additionaldetails = tk.StringVar()
        self.df = pd.DataFrame()

        # Define Widgets
        self.title("Employee Management System") #title of the gui
        self.geometry("940x540+20+90")           #determines the size of the windpw
        self.configure(bg='grey')                #determines the colour of the background of the window


        #Frame which contains other widgets
        frame = tk.Frame(self)
        frame.grid(row=0, column=0, columnspan=4)
        frame.configure(bg='black')
        #field label,entry box and its position for employeeID variable
        field_label = tk.Label(frame, text="employeeID", font=("Comic sans ms", 12))
        field_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.text_employeeID = tk.Entry(frame, textvariable=self.employeeID, font=("Comic sans ms", 12), width=15)
        self.text_employeeID.grid(row=0, column=1, padx=10, pady=15, stick="w")
        # field label,entry box and its position for first name variable
        field_label = tk.Label(frame, text="first name", font=("Comic sans ms", 12))
        field_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.text_firstname = tk.Entry(frame, textvariable=self.firstname, font=("Comic sans ms", 12), width=15)
        self.text_firstname.grid(row=1, column=1, padx=10, pady=15, stick="w")
        # field label,entry box and its position for last name variable
        field_label = tk.Label(frame, text="last name", font=("Comic sans ms", 12))
        field_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.text_lastname = tk.Entry(frame, textvariable=self.lastname, font=("Comic sans ms", 12), width=15)
        self.text_lastname.grid(row=2, column=1, padx=10, pady=15, stick="w")
        # field label,entry box and its position for email address variable
        field_label = tk.Label(frame, text="Email Address", font=("Comic sans ms", 12))
        field_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.text_email = tk.Entry(frame, textvariable=self.email, font=("Comic sans ms", 12), width=15)
        self.text_email.grid(row=3, column=1, padx=10, pady=15, stick="w")
        # field label,entry box and its position for gender variable
        field_label = tk.Label(frame, text="gender", font=("Comic sans ms", 12))
        field_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.text_gender = tk.Entry(frame, textvariable=self.gender, font=("Comic sans ms", 12), width=15)
        self.text_gender.grid(row=4, column=1, padx=10, pady=15, stick="w")
        # field label,entry box and its position for contact number variable
        label_contactnumber = tk.Label(frame, text="contact number", font=("Comic sans ms", 12))
        label_contactnumber.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.text_contactnumber = tk.Entry(frame, textvariable=self.contactnumber, font=("Comic sans ms", 12), width=15)
        self.text_contactnumber.grid(row=5, column=1, padx=10, pady=15, stick="w")
        # field label,entry box and its position for Role variable
        field_label = tk.Label(frame, text="Role", font=("Comic sans ms", 12))
        field_label.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.text_Role = tk.Entry(frame, textvariable=self.Role, font=("Comic sans ms", 12), width=15)
        self.text_Role.grid(row=0, column=3, padx=10, pady=15, stick="w")
        #field label,entry box and its position for Salary variable
        field_label = tk.Label(frame, text="Salary", font=("Comic sans ms", 12))
        field_label.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.text_salary = tk.Entry(frame, textvariable=self.salary, font=("Comic sans ms", 12), width=15)
        self.text_salary.grid(row=1, column=3, padx=10, pady=15, stick="w")
        #field label,entry box and its position for country variable
        field_label = tk.Label(frame, text="country", font=("Comic sans ms", 12))
        field_label.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.text_country = tk.Entry(frame, textvariable=self.country, font=("Comic sans ms", 12), width=15)
        self.text_country.grid(row=2, column=3, padx=10, pady=15, stick="w")
        #field label,entry box and its position for Emergency Contact variable
        field_label = tk.Label(frame, text="Emergency Contact", font=("Comic sans ms", 12))
        field_label.grid(row=3, column=2, padx=10, pady=10, sticky="w")
        self.text_EmergencyContact = tk.Entry(frame, textvariable=self.EmergencyContact, font=("Comic sans ms", 12), width=15)
        self.text_EmergencyContact.grid(row=3, column=3, padx=10, pady=15, stick="w")
        #field label,entry box and its position for DOB variable
        field_label = tk.Label(frame, text="DOB", font=("Comic sans ms", 12))
        field_label.grid(row=4, column=2, padx=10, pady=10, sticky="w")
        self.text_DOB = tk.Entry(frame, textvariable=self.DOB, font=("Comic sans ms", 12), width=15)
        self.text_DOB.grid(row=4, column=3, padx=10, pady=15, stick="w")
        #field label,entry box and its position for shift variable
        field_label = tk.Label(frame, text="full time/part time", font=("Comic sans ms", 12))
        field_label.grid(row=5, column=2, padx=10, pady=15, sticky="w")
        self.text_shift = tk.Entry(frame, textvariable=self.shift, font=("Comic sans ms", 12), width=15)
        self.text_shift.grid(row=5, column=3, padx=10, pady=15, stick="w")
        #field label,entry box and its position for Additional details variable
        field_label = tk.Label(frame, text="Additional Details", font=("Comic sans ms", 12))
        field_label.grid(row=6, column=0, padx=10, pady=15, sticky="w")
        self.text_additionaldetails = tk.Entry(frame, textvariable=self.additionaldetails, font=("Comic sans ms", 12), width=15)
        self.text_additionaldetails.grid(row=6, column=1, padx=10, pady=15, stick="w")




        #button
        Button = tk.Frame(frame)
        Button.grid(row=10, column=0, columnspan=4, padx=10, pady=10, sticky="w")
        Button.configure(bg='grey')#background colour of button
        # Button Widgets
        tk.Button(Button, command=self.load_file, text="Load File", width=15, font=("Comic sans ms", 12, "bold")).grid(
            row=0, column=0)#Load file button along with position, font type and font size

        tk.Button(Button, command=self.enter_record, text="Enter Record", width=15,
                  font=("Comic sans ms", 12, "bold")).grid(
            row=0, column=1, padx=10)#Enter record button with position,font type and font size

        tk.Button(Button, command=self.save_file, text="Save File", width=15, font=("Comic sans ms", 12, "bold")).grid(
            row=0, column=2, padx=10)#Save File button with position, font type and font size
        #creation of treeview frame
        tree_frame = ttk.Frame(self)
        tree_frame.place(x=0, y=470, width=820, height=200)#positon and size of treeview frame

        # Treview style
        style = ttk.Style(self)
        style.theme_use('winnative')
        style.configure('Treeview', font=('Comic sans ms', 10), columnwidth=10,
                        rowheight=20, background='white', fieldbackground='white')  # Modify the font of the body
        style.configure('Treeview.Heading', font=('Comic sans ms', 10))  # Modify the font of the headings
        style.map('Treeview', backgound=[('selected', 'blue')])
        style.configure('TFrame', background='white')

        self.tv = ttk.Treeview(tree_frame, columns=(1, 2, 3,), show='headings')

        #vertical scroll bar for treeview widget
        vscrollbar = ttk.Scrollbar(tree_frame, orient=VERTICAL)
        vscrollbar.pack(side=RIGHT, fill=Y)

        self.tv.config(yscrollcommand=vscrollbar.set)
        vscrollbar.config(command=self.tv.yview)
        #horizontal scroll bar for treeview widget
        hscrollbar = ttk.Scrollbar(tree_frame, orient=HORIZONTAL)
        hscrollbar.pack(side=BOTTOM, fill=X)

        self.tv.config(xscrollcommand=hscrollbar.set)
        hscrollbar.config(command=self.tv.xview)

        # bind to double cick to select
        self.tv.bind('<Double-1>', "")
        #function allowing for loading files
    def load_file(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select A File",
                                              filetype=(("xlsx files", "*.xlsx"), ("All Files", "*.*")))

        if filename[-4:] == 'xlsx':
            self.df = pd.read_excel(filename)
            # print(self.df)
            self.showAll()
        else:
            messagebox.showerror("file not recognised")

        #function which makes the completion of certain fields mandatory
    def enter_record(self):
        if self.text_employeeID.get()=="" or self.text_DOB.get()=="" or self.text_firstname.get()=="" or self.text_lastname.get()=="" \
                or self.text_additionaldetails.get()=="" or self.text_EmergencyContact==""\
                or self.text_gender.get()=="" or self.text_email.get()=="" or self.text_Role.get()=="" \
                or self.text_contactnumber=="" or self.text_salary.get()=="" or self.text_shift.get()=="" :
            messagebox.showerror("Please Complete all Fields")
        else:
            dict = {'employeeID':self.firstname.get(),'firstname':self.firstname.get(),'lastname':self.lastname.get(),
                    'additionaldetails':self.additionaldetails.get(),'gender':self.gender.get(),'email':self.email.get(),'Role':self.Role.get(),
                    'contact number':self.contactnumber.get(),'salary':self.salary.get(),'shift':self.shift.get(),'DOB':self.shift.get(),
                    'Emergency Contact':self.text_EmergencyContact.get(),
                    }
            self.df = self.df.append(dict,ignore_index=True)
            # print(self.df)
            self.clear_boxes()
            self.showAll()
        #function which displays contents of the treeview widget
    def showAll(self):


        self.tv.delete(*self.tv.get_children())
        self.tv["column"] = list(self.df.columns)
        self.tv["show"] = "headings"
        #creates headings
        for column in self.tv["columns"]:
            self.tv.heading(column, text=column)  #let the column heading = column name

        df_rows = self.df.to_numpy().tolist()  #turns the dataframe into a list of lists
        for row in df_rows:
            self.tv.insert("", "end", values=row)  #inserts each list into the treeview. For parameters see
        self.tv.pack(side=LEFT)
      #function which allows for the clearance of boxes follwowing entry
    def clear_boxes(self):
        self.employeeID.set(0, END)
        self.firstname.set(0, END)
        self.lastname.set(0, END)
        self.gender.set(0, END)
        self.email.set(0, END)
        self.contactnumber.set(0, END)
        self.Role.set(0, END)
        self.salary.set(0, END)
        self.country.set(0, END)
        self.EmergencyContact.set(0, END)
        self.shift.set(0, END)
        self.DOB.set(0, END)
        self.additionaldetails.set(0, END)

    def save_file(self):
    #     """This Function will open the asksaveasfile dilaog save data to an excel or csv file"""

        files = [('excel file', '*.xlsx'), ('All Files', '*.*')]
        filename = asksaveasfile(filetypes=files, defaultextension=files)
        #print(filename)

        if filename.name[-4:] == 'xlsx':
            writer = pd.ExcelWriter(filename.name)
            self.df.to_excel(writer)
            writer.save()
        else:
            messagebox.showerror("Cannot Save File")

# Press the play button to run the script.
if __name__ == '__main__':
    app = EmployeeManagementGUI()
    app.mainloop()




