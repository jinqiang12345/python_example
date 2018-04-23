from openpyxl import Workbook

wb = Workbook()
sheet = wb.active
sheet.title = "qiang"
sheet["C3"] = "hello world!"
for i in range(10):
    m = i + 1
    sheet["A{0}".format(m)].value = m
wb.save("D:/highpython/Python-master/learn/zzz.xlsx")