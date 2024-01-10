import pandas as pd

wb = pd.read_excel(
    'https://stepik.org/media/attachments/lesson/245266/tab.xlsx')
print(min(wb.iloc[6:27, 2]))
