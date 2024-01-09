import requests
import re
from collections import Counter

res = requests.get('https://stepik.org/media/attachments/lesson/209719/2.html')

spisok = Counter(re.findall(r'<code>(.*?)</code>', res.text))

print(*[i[0] for i in spisok.items() if i[1] == max(spisok.values())])
