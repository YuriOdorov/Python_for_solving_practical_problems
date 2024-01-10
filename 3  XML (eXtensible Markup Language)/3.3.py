import xmltodict
import requests

req = requests.get(
    'https://stepik.org/media/attachments/lesson/245681/map2.osm').content
parsedxml = xmltodict.parse(req)
counter = 0
for node in parsedxml['osm']['node']:
    if 'tag' in node:
        if type(node['tag']) is list:
            for tag in node['tag']:
                if tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                    counter += 1
        elif node['tag']['@k'] == 'amenity' and node['tag']['@v'] == 'fuel':
            counter += 1
print(counter)
