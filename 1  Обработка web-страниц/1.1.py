import requests

res = requests.get('https://stepik.org/media/attachments/lesson/209717/1.html')

print('python:', res.text.lower().count('python'), '|| c++:',
      res.text.lower().count('c++'))
