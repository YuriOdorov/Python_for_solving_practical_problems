import xmltodict
import requests

req = requests.get(
    'https://stepik.org/media/attachments/lesson/245678/map1.osm').content
parsedxml = xmltodict.parse(req)
res = sum('tag' in i for i in parsedxml['osm']['node'])
print(res, len(parsedxml['osm']['node']) - res)
