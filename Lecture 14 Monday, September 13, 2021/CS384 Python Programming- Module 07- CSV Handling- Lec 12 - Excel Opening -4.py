import openpyxl
import os
from openpyxl.styles import Font, colors
os.chdir(r"C:\Users\Ganapathy\Dropbox\CS384 2021 (7)\Lecture 14 Monday, September 13, 2021")
wb = openpyxl.load_workbook('sample_file.xlsx')

sheet = wb.active

x1 = sheet['A1']
x2 = sheet['A2']
# using cell() function
sheet['A1'].font = Font(size = 12, name = 'Century', bold = True, color = "FF0000")
sheet.cell(row = 5, column=5).value = 10
print("The first cell value:", x1.value)
print("The second cell value:", x2.value)
# print("The third cell value:", x3.value)
wb.save('sample_file.xlsx')