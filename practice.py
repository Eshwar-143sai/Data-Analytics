import pandas as pd
excel_path = r'C:\Users\saies\Downloads\sample_employee_data.xlsx'
df = pd.read_excel(excel_path)
print(df.head())

