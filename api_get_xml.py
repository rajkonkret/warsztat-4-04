import requests as re
import xml.etree.ElementTree as ET

# response = re.get('http://api.weatherapi.com/v1/current.json?key=d863af85e8fa43618f682810220812&q=Lublin&aqi=no')
response = re.get('http://api.nbp.pl/api/exchangerates/rates/A/EUR/?format=xml')


xml_data = response.content
print(xml_data)
root = ET.fromstring(xml_data)
print(root.attrib)

for child in root:
    print(child.tag, child.attrib)

print([elem.tag for elem in root.iter()])

for rate in root.find('Rates'):
    print(rate.attrib)