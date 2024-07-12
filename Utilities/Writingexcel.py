import openpyxl

path = "../testdata/Login.xlsx"


def writeExcel(sheetname, row, column, text):
    workbook = openpyxl.load_workbook("../testdata/Login.xlsx")
    sheet = workbook[sheetname]
    sheet.cell(row=row,column=column).value=text
    workbook.save(path)


writeExcel("LoginPage",4,1,"Team1")

