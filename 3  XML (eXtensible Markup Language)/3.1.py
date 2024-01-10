import xmltodict
import requests

req = requests.get(
    'https://stepik.org/media/attachments/lesson/245571/map1.osm').content
parsedxml = xmltodict.parse(req)
print(parsedxml['osm']['node'][100]['@id'])
