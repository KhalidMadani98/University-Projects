from tkinter.filedialog import asksaveasfile
import pandas as pd
from tkinter import ttk, messagebox, filedialog
class EmployeeData:
# def __init__(self):
#   pass

    @staticmethod
#load file function from GUI
    def load_file():
        filename = filedialog.askopenfilename(initialdir="/",
                                              title="Select A File",
                                              filetype=(("xlsx files", "*.xlsx"), ("All Files", "*.*")))
        filename = r"{}".format(filename)
        #print(excel_filename)
        df= pd.DataFrame()
        try:
            if filename[-4:] == 'xlsx':
                df = pd.read_excel(filename)
        except ValueError:
            messagebox.showerror('This type of file { } is not handled in this table'.format(filename[-4]))
        else:
            return df


    @staticmethod
#save file function from GUI
    def save_file(self):

        files = [('excel file', '*.xlsx'), ('All Files', '*.*')]
        filename = asksaveasfile(filetypes=files, defaultextension=files)
        print(filename.name)

        if filename.name[-4:] == 'xlsx':
            writer = pd.ExcelWriter(filename.name)
            self.df.to_excel(writer)
            writer.save()

        else:
            raise ValueError('This type of file { } is not handled in this table'.format(filename.name[-4:]))

    @staticmethod
#load file function for testing
    def load_file_withoutgui(filename):
        excel_filename = r"{}".format(filename)
        #print(excel_filename)
        df = pd.DataFrame()

        try:
            if excel_filename[-4:] == 'xlsx':
                df = pd.read_excel(filename)

        except ValueError:
            pass
        # messagebox.showerror('File type { } not handled in this table'.format(excel_filename[-4]))
        except FileNotFoundError:
            pass
        # messagebox.showerror("Information", f"No such file as {excel_filename}")
        else:
                return df

    @staticmethod
#save file function for testing
    def save_file_withoutgui(self, filename):
            if filename[-4:] == 'xlsx':
                writer = pd.ExcelWriter(filename)
                self.data_frame.to_excel(writer)
                writer.save()

                self.data_frame.to_csv(filename, index=False, header=True)
            else:
                raise ValueError('This File type {} is not handled in this table'.format(filename[-4:]))
