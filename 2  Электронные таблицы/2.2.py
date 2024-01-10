import pandas as pd

wb = pd.read_excel(
    'https://stepik.org/media/attachments/lesson/245267/salaries.xlsx')
a = wb.set_index('Unnamed: 0').T.quantile(0.5)
b = wb.describe().mean()
print(a[a == max(a)].index[0], b[b == max(b)].index[0])
