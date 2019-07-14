import xlwings as xw    # for excel-python integration
import pandas as pd     # for dataframe     
import numpy as np      # for NaN values
import win32api         # for message box



# ==================================GLOBAL INPUTS===================================================================================================================
excel_file_directory__biometric = 'I:\\github_repos\\BioM\\data\\IntnlCmpsReport.xls'
excel_file_directory__employee_record = 'I:\\github_repos\\BioM\\data\\employee_record.xlsx'
sht_data_biometric = 'IntnlCmpsReport'
sht_data_employeerecord = 'VMFG Employees'
sht_main = 'Main'
columns_required = ['Emp Code', 'Emp Name', 'Reader', 'Date', 'Time', 'Status']



#=================================================================MAIN FUNCTION======================================================================================
def main():
    wb = xw.Book.caller()
    # wb.sheets[0].range("A1").value = "Hello xlwings!"

    #----------------------------------------------------------------------------------------------------------------------------------------------------------------    
    # Sheet definition
    sht_biom = wb.sheets[sht_main]
    sht_run_code = wb.sheets['RUN_code']

    # from 'Biometric' data
    df_biom = pd.ExcelFile(excel_file_directory__biometric).parse(sht_data_biometric, skiprows= 11)

    # from 'Employees' data maintained for attendance record
    df_employees = pd.ExcelFile(excel_file_directory__employee_record).parse(sht_data_employeerecord, skiprows= 1)
    section_vmfg_list = df_employees['Section'].tolist()

    # Filtering, Removing the repeated column headers
    df_biom = df_biom.drop(['Unnamed: 0', 'Sr.No.'], axis=1)      # drop columns with header names - ['Unnamed: 0', 'Sr.No.']
    df_biom = df_biom[(df_biom['Reader'] != 'Reader') & (df_biom['Reader'] != 'NaN')]       # delete rows with values - 'Reader' & 'NIL'
    df_biom.fillna(method= 'ffill', inplace=True)    # fill 'NaN' with previous values using 'ffill'
    df_biom = df_biom[(df_biom['Reader'] == 'M FAB - 1') | (df_biom['Reader'] == 'M FAB')]      # extract dataframe with column header names - 'M FAB - 1' or 'M FAB'
    df_biom.insert(2, column= "Section", value= np.nan)          # Insert 'Section' column
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------    
    # designate section to the corresponding employee name
    biom_emp_list = df_biom['Emp Name'].tolist()
    # create a NEW biom_employee_list to include names without `space` in the end of string
    biom_emp_list_new = []
    
    # loop in the old biom_emp_list and append new string to new biom_emp_list_new
    for emp in biom_emp_list:
        biom_emp_list_new.append(emp.rstrip())

    # assign biom section list to include the 'Section' corresponding to employees in BIOM employee column
    df_biom_section_list = []
    for emp in biom_emp_list_new:
        if df_employees[df_employees['Name'].isin([emp])].empty == False:
            df_biom_section_list.append(df_employees.loc[df_employees['Name'] == emp, 'Section'].iloc[0])
        else:
            win32api.MessageBox(wb.app.hand, "Employee name - {0} doesn't match".format(emp), "Error in Employee records")

    df_biom['Section'] = df_biom_section_list
    
    #--------------------------------------------------------------------------------------------------------------------------------    
    # display output to Excel sheet - 'Main'
    sht_biom.clear()        # Clear the content and formatting before displaying the data
    sht_biom.range('A1').options(index=False).value = df_biom         # show the dataframe values into sheet- 'RUN_code'
    sht_biom.range('A1:Z1048576').autofit()     # autofit the entire excel sheet


# -------------------------------------------------------MAIN function------------------------------------------------------------------------------------------------
# if __name__ == '__main__':
#     main()


#--------------------------------------------------------------------------------------------------------------------------------
# User Defined Functions (UDFs)
#--------------------------------------------------------------------------------------------------------------------------------
# @xw.func
# def hello(name):
#     return "hello {0}".format(name)
