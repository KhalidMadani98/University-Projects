from tkinter.filedialog import asksaveasfile
import pandas as pd
from tkinter import ttk, messagebox, filedialog

class EmployeeManagementGUI:
# def __init__(self):
#   pass
    @staticmethod
    def load_file(self):
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select A File",
                                              filetype=(("xlsx files", "*.xlsx"), ("All Files", "*.*")))
        filename = r"{}".format(filename)
        #print(excel_filename)
        self.df= pd.DataFrame()
        try:
            if filename[-4:] == 'xlsx':
                self.df = pd.read_excel(filename)
        except ValueError:
            messagebox.showerror('This type of file { } is not handled in this table'.format(filename[-4]))
        else:
            return self.df

    def save_file(self):
    #     """This Function will open the asksaveasfile dilaog save data to an excel or csv file"""

        files = [('excel file', '*.xlsx'), ('All Files', '*.*')]
        filename = asksaveasfile(filetypes=files, defaultextension=files)
        #print(filename)

        if filename.name[-4:] == 'xlsx':


    def save_data(df):

        files = [('excel file', '*.xlsx'),
                 ('csv file', '*.csv'),
                 ('All Files', '*.*')]
        filename = asksaveasfile(filetypes=files, defaultextension=files)
        print(filename.name)

        if filename.name[-4:] == 'xlsx':
            writer = pd.ExcelWriter(filename.name)
            df.to_excel(writer)
            writer.save()
        elif filename.name[-4:] == 'csv':

            df.to_csv(filename.name, index=False, header=True)
        else:
            raise ValueError('File type {} not handled in this table'.format(filename.name[-4:]))
