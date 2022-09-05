import pandas as pd

dfexcel = pd.read_excel("Dados Excel.xlsx", sheet_name=1)
dfcsv = pd.read_csv("Dados aula 1.csv", encoding = "UTF-8", sep = ";", usecols=["AddressID", "AddressLine1"], nrows=200)

arquivo_excel = pd.ExcelFile("Dados Excel.xlsx")
print(arquivo_excel.sheet_names)
aba1 = arquivo_excel.parse('Dados Excel')
aba2 = arquivo_excel.parse('segunda')
print(aba1)
print(aba2)
#print(dfexcel.head())
#print(dfcsv.head())
