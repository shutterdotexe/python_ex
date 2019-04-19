from urllib.request import urlopen as uReq
import xml.etree.ElementTree as ET
myUrl = 'http://py4e-data.dr-chuck.net/comments_129031.xml'
connection = uReq(myUrl)
xmlFile = connection.read()
connection.close()
tree = ET.fromstring(xmlFile)
lst = tree.findall('.//count')
print('Count: ', len(lst))
total = list()
counting = 0
for item in lst:
    total.append(int(item.text))
print(sum(total))
