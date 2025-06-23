import unittest
import pandas as pd
from EmployeeManagementGUI import EmployeeManagementGUI
from employee import EmployeeData

class EmployeeManagementTest(unittest.TestCase):#what i call my called my something ttk
#example data from file
    def setUp(self):

        self.dict = {'employeeID': '1',
                     'first name': 'Herb',
                     'last name': 'Hadwen',
                     'email': 'hhadwen0@usgs.gov',
                     'gender': 'Male',
                     'contact number': '678-569-9351',
                     'Role': 'GIS Technical Architect',
                     'Salary': '92.233.155.61',
                     'Country': 'China',
                     'Emergency Contact':'431-343-7009',
                     'DOB':'12/05/2021',
                     'Full Time/Part Time':'Full Time',
                     'Additional details':'CSA qualified'
                     }
#pass function
    def tearDown(self):
        pass


#function for testing load file
    def test_load_file(self):
        my_filepathway = r"C:\Users\MADANIS\PycharmProjects\pythonProject9\EmployeeManagementData.xlsx"#file pathway for excel file
        name_file = 'Samplefile.xlsx'#name of saved file
        filename = my_filepathway+name_file
        my_dict = EmployeeData().load_file_withoutgui(filename).to_dict()

        f_name = my_dict['employeeID']
        data_frame = f_name[0]
        data_name= self.dict['employeeID']
        #change all variables
        print(data_frame)
        print(data_name)
        self.assertqual(data_frame, data_name)
#function to test save file
    def test_save_file(self):
        my_filepathway = r"C:\Users\MADANIS\PycharmProjects\pythonProject9\EmployeeManagementData.xlsx"#insert filepathway
        my_filename = 'SamplefileSave.xlsx'#name of saved file
        my_samplefile = 'Samplefile.xlsx'
        my_filename = my_filepathway + my_filename
        test_filename = my_filepathway+my_samplefile

        data_frame = pd.DataFrame(self.dict,index=[0])

        EmployeeData().save_file_withoutgui(data_frame,my_filename)
        my_dict = EmployeeData().load_file_withoutgui(test_filename).to_dict()

        f_name = my_dict['employeeID']
        data_frame = f_name[0]
        data_name = self.dict['employeeID']

        print(df_name)
        print(d_name)
        self.assertEqual(data_frame, data_name)#allows for run of unit testing


if __name__ == '__main__':
    unittest.main()
