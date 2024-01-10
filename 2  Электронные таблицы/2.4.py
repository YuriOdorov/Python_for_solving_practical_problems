import io
import zipfile
import requests
import pandas as pd

r = requests.get(
    "https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip")

with r, zipfile.ZipFile(io.BytesIO(r.content)) as archive:
    member = archive.infolist()[0]
    wb = pd.read_excel(archive.read(member))[['Unnamed: 1', 'Unnamed: 3']] \
        .head(1)
    for member in archive.infolist()[1:]:
        wb2 = pd.read_excel(archive.read(member))[
            ['Unnamed: 1', 'Unnamed: 3']].head(1)
        wb = pd.concat([wb, wb2])
wb = wb.sort_values('Unnamed: 1')
wb['Unnamed: 3'] = wb['Unnamed: 3'].astype('int')
[print(*wb.iloc[i]) for i in range(len(wb))]
