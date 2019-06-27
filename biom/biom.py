import xlwings as xw
import pandas as pd


excel_file_directory = 'I:\\github_repos\\BioM\\data\\IntnlCmpsReport.xls'
sht_data = 'IntnlCmpsReport'
sht_main = 'Main'
columns_required = ['Emp Code', 'Emp Name', 'Reader', 'Date', 'Time', 'Status']



def main():
    wb = xw.Book.caller()
    # wb.sheets[0].range("A1").value = "Hello xlwings!"

    #----------------------------------------------------------------------------------------------------------------------------------------------------------------    
    # Sheet definition
    sht_biom = wb.sheets[sht_main]
    sht_run_code = wb.sheets['RUN_code']

    excel_file = pd.ExcelFile(excel_file_directory)
    df = excel_file.parse(sht_data, skiprows= 11)

    df = df.drop(['Unnamed: 0', 'Sr.No.'], axis=1)      # drop columns with header names - ['Unnamed: 0', 'Sr.No.']
    df = df[(df['Reader'] != 'Reader') & (df['Reader'] != 'NaN')]       # delete rows with values - 'Reader' & 'NIL'
    df.fillna(method= 'ffill', inplace=True)    # fill 'NaN' with previous values using 'ffill'
    df = df[(df['Reader'] == 'M FAB - 1') | (df['Reader'] == 'M FAB')]      # extract dataframe with column header names - 'M FAB - 1' or 'M FAB'
    # print(df)
    #----------------------------------------------------------------------------------------------------------------------------------------------------------------    
    # display output to Excel sheet - 'Main'
    sht_biom.clear()        # Clear the content and formatting before displaying the data
    sht_biom.range('A1').options(index=False).value = df         # show the dataframe values into sheet- 'RUN_code'
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
