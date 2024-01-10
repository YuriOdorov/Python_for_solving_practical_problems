from bs4 import BeautifulSoup
import requests

req = requests.get(
    'https://stepik.org/media/attachments/lesson/245681/map2.osm').content
soup = BeautifulSoup(req, features="xml")
print(len(soup.select('tag[k=amenity][v=fuel]')))

# import xmltodict
# import requests
# req = requests.get('https://stepik.org/media/attachments/lesson/245681/map2.osm').content
# dct = xmltodict.parse(req)
# counter = 0
# for node in (dct['osm']['node'] + dct['osm']['way']):
#     if 'tag' in node:
#         if type(node['tag']) is list:
#             for tag in node['tag']:
#                 if tag['@k'] =='amenity' and  tag['@v'] == 'fuel':
#                     counter += 1
#         elif node['tag']['@k'] == 'amenity' and node['tag']['@v'] == 'fuel':
#             counter += 1
# print(counter)
