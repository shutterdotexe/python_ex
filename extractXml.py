#This program is reading and extracting the xml from a
#specified Url address, counts the count tags in the whole
# xml file and prints the sum of those values
from urllib.request import urlopen as uReq
import xml.etree.ElementTree as ET
myUrl = 'http://py4e-data.dr-chuck.net/comments_129031.xml'
connection = uReq(myUrl)
xmlFile = connection.read()
connection.close()
tree = ET.fromstring(xmlFile)
lst = tree.findall('.//count')
#checking for how many counts I've got
print('Count: ', len(lst))
total = list()
#counting = 0
for item in lst:
    total.append(int(item.text))
print(sum(total))
#just some modifications to see the behaviour of git  