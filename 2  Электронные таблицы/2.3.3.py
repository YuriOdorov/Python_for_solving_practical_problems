import pandas as pd

wb = pd.read_excel(
    'https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx')
wb = wb.fillna(0)
wb2 = pd.read_excel(
    'https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx',
    sheet_name='Раскладка')
wb2 = wb2.fillna(0)
wb = wb.merge(wb2, left_on='Unnamed: 0', right_on='Продукт')
wb['ККал'] = wb['ККал на 100'] * (wb['Вес в граммах'] / 100)
wb['Б'] = wb['Б на 100'] * (wb['Вес в граммах'] / 100)
wb['Ж'] = wb['Ж на 100'] * (wb['Вес в граммах'] / 100)
wb['У'] = wb['У на 100'] * (wb['Вес в граммах'] / 100)
print(*wb[['ККал', 'Б', 'Ж', 'У']].agg(sum).astype('int'))
