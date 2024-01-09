from urllib.request import urlopen
from bs4 import BeautifulSoup

resp = urlopen(
    ' https://stepik.org/media/attachments/lesson/209723/3.html')  # скачиваем файл
html = resp.read().decode('utf8')  # считываем содержимое
soup = BeautifulSoup(html, 'html.parser')  # делаем суп

summ = 0
table = soup.select('table')[0]
for tr in table.select('tr'):
    tds = tr.select('td')
    for td in tds:
        summ += int(td.text.strip())
print(summ)
