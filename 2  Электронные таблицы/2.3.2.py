import pandas as pd

wb = pd.read_excel(
    'https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx')
print(*wb.fillna(0).sort_values(['ККал на 100', 'Unnamed: 0'],
                                ascending=[False, True])['Unnamed: 0'].tolist(),
      sep='\n')
