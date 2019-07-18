import xlwings as xw    # for excel-python integration
import pandas as pd     # for dataframe     
import numpy as np      # for NaN values
import win32api         # for message box
import plotly as py
from plotly.graph_objs import Pie



# ===========================================================================GLOBAL INPUTS=========================================================================
excel_file_directory__biometric = 'I:\\github_repos\\BioM\\data\\IntnlCmpsReport.xls'
excel_file_directory__employee_record = 'I:\\github_repos\\BioM\\data\\employee_record.xlsx'
sht_data_biometric = 'IntnlCmpsReport'
sht_data_employeerecord = 'VMFG Employees'
sht_main = 'Main'
columns_required = ['Emp Code', 'Emp Name', 'Reader', 'Date', 'Time', 'Status']

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
"Description": This is a pie chart b/w Section vs employee_count
"values": employee_count
"labels": Section/Division's list
'''
def biom_pie_plot(values, labels):
    trace1 = Pie(
        values= values,
        labels= labels,
        name= "Section's Employees count",
        textinfo= 'label+value'
        # hoverinfo= "label+value+percent+name",
        # hole=0.2
        )
    data = [trace1]
    layout= dict(
        title= "Section's Employees count",
        # annotations= [
        #     dict(
        #         font= {"size": 20},
        #         showarrow= False,
        #         text= "Section's Employees count",
        #         x= 0.5,
        #         y= 0.5
        #         )
        #     ]
        )

    fig = dict(data= data, layout= layout)
    py.offline.plot(fig, filename= 'Section_Employees_count.html')


#================================================================================MAIN FUNCTION========================================================================
def main():
    # wb = xw.Book.caller()
    # wb.sheets[0].range("A1").value = "Hello xlwings!"

    #----------------------------------------------------------------------------------------------------------------------------------------------------------------    
    # Sheets
    # sht_biom = wb.sheets[sht_main]
    # sht_test = wb.sheets['test']
    # sht_run_code = wb.sheets['RUN_code']

    #----------------------------------------------------------------------------------------------------------------------------------------------------------------    
    # from 'Biometric' data
    df_biom = pd.ExcelFile(excel_file_directory__biometric).parse(sht_data_biometric, skiprows= 11)

    # from 'Employees' data maintained for attendance record
    df_employees = pd.ExcelFile(excel_file_directory__employee_record).parse(sht_data_employeerecord, skiprows= 1)
    # section_vmfg_list = df_employees['Section'].tolist()

    # Filtering, Removing the repeated column headers
    df_biom = df_biom.drop(['Unnamed: 0', 'Sr.No.'], axis=1)      # drop columns with header names - ['Unnamed: 0', 'Sr.No.']
    df_biom = df_biom[(df_biom['Reader'] != 'Reader') & (df_biom['Reader'] != 'NaN')]       # delete rows with values - 'Reader' & 'NIL'
    df_biom.fillna(method= 'ffill', inplace=True)    # fill 'NaN' with previous values using 'ffill'
    df_biom = df_biom[(df_biom['Reader'] == 'M FAB - 1') | (df_biom['Reader'] == 'M FAB')]      # extract dataframe with column header names - 'M FAB - 1' or 'M FAB'
    df_biom.insert(2, column= "Section", value= np.nan)          # Insert 'Section' column
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------    
    # designate section to the corresponding employee name
    biom_empcode_list = df_biom['Emp Code'].tolist()

    # assign biom section list to include the 'Section' corresponding to employees in BIOM employee column
    df_biom_section_list = []
    for empcode in biom_empcode_list:
        if df_employees[df_employees['Employee Code'].isin([empcode])].empty == False:
            df_biom_section_list.append(df_employees.loc[df_employees['Employee Code'] == empcode, 'Section'].iloc[0])
        else:
            win32api.MessageBox(wb.app.hand, "Employee name - {0} doesn't match".format(empcode), "Error in Employee records")
    df_biom['Section'] = df_biom_section_list
    
    #--------------------------------------------------------------------------------------------------------------------------------    
    # # display output to Excel sheet - 'Main'
    # sht_biom.clear()        # Clear the content and formatting before displaying the data
    # sht_biom.range('A1').options(index=False).value = df_biom         # show the dataframe values into sheet- 'RUN_code'
    # sht_biom.range('A1:Z1048576').autofit()     # autofit the entire excel sheet

    #---------------------------------------------------Pie Chart-----------------------------------------------------------------    
    '''
    TODO:
    + filter-out GH-VMFG
    - 
    '''
    df_biom_pie_plot = df_biom[df_biom['Section'] != 'GH']      # filter-out 'GH' from dataframe
    df_biom_pie_plot = df_biom_pie_plot[['Emp Code', 'Section']].drop_duplicates()
    df_biom_pie_plot_values = df_biom_pie_plot['Section'].value_counts()
    df_biom_pie_plot_labels = df_biom_pie_plot['Section'].value_counts().index

    # sht_test.clear()        # Clear the content and formatting before displaying the data
    # sht_test.range('A1').options(index=False).value = df_biom_pie_plot         # show the dataframe values into sheet- 'RUN_code'
    # sht_test.range('A1:Z1048576').autofit()     # autofit the entire excel sheet

    # Create a pie chart
    biom_pie_plot(
        values= df_biom_pie_plot_values, 
        labels= df_biom_pie_plot_labels
        )

    #---------------------------------------------------Bubble Chart-----------------------------------------------------------------    


# -------------------------------------------------------MAIN function------------------------------------------------------------
if __name__ == '__main__':
    main()


#--------------------------------------------------------------------------------------------------------------------------------
# User Defined Functions (UDFs)
#--------------------------------------------------------------------------------------------------------------------------------
# @xw.func
# def hello(name):
#     return "hello {0}".format(name)
