import pandas as pd

excel_data = pd.read_excel('sales.xlsx')

data = pd.DataFrame(excel_data, columns=['Sales Date', 'Sales Person', 'Cena'])

print("The content is:\n", data)
print(type(data))
print(data.columns)
print(data.values)

data_2 = pd.DataFrame(excel_data)
values = data_2['Amount'].tolist()
print(data_2)
print(values)