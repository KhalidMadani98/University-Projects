from tkinter.filedialog import asksaveasfile
import pandas as pd
from tkinter import ttk, messagebox, filedialog

class EmployeeManagementData:
    #def __init__(self):
    #   pass

    @staticmethod
    def load_data():

        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select A File",
                                              filetype=(("xlsx files", "*.xlsx"), ("All Files", "*.*")))
        excel_filename = r"{}".format(filename)
        #print(excel_filename)
        df = pd.DataFrame()

        try:
            if excel_filename[-4:] == 'xlsx':
                df = pd.read_excel(filename)

            elif excel_filename[-4:] == 'csv':
                df = pd.read_csv(filename)
        except ValueError:
            messagebox.showerror('File type { } not handled in this table'.format(excel_filename[-4]))
        except FileNotFoundError:
            messagebox.showerror("Information", f"No such file as {excel_filename}")
        else:
            return df

    @staticmethod
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

    @staticmethod
    def load_data_withoutgui(self,filename):
        excel_filename = r"{}".format(filename)
        #print(excel_filename)
        self.df = pd.DataFrame()

        try:
            if excel_filename[-4:] == 'xlsx':
                self.df = pd.read_excel(filename)

        except ValueError:
            pass
        # messagebox.showerror('File type { } not handled in this table'.format(excel_filename[-4]))
        else:
                return self.df

    @staticmethod
    def save_data_nogui(df,filename):
        if filename[-4:] == 'xlsx':
            writer = pd.ExcelWriter(filename)
            df.to_excel(writer)
            writer.save()
        elif filename.name[-4:] == 'csv':

            df.to_csv(filename, index=False, header=True)
        else:
            raise ValueError('File type {} not handled in this table'.format(filename[-4:]))

    def save_data(self,filename):

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