import pandas as pd

# xlsx = pd.ExcelFile('主机号.xlsx', engine='openpyxl')
xlsx = pd.read_excel('/Users/sven/PycharmProjects/123/读取表格/主机号.xlsx')
# print(type(xlsx))
# print(xlsx)
for i in xlsx:
	print(i)
	print(xlsx)
