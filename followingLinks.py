from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#reading URL from user's input
myUrl = input('Please enter your URL: ')
#the position of the link you want
linkNumber = int(input('Please enter the link number: ')) - 1
#the number of times you want to loop this
count = int(input('Please enter count: '))

while count > 0:

    connection = uReq(myUrl)
    readingFile = connection.read()
    page_soup = soup(readingFile, "html.parser")
    tags = page_soup('a')
    #extracting the URL from the position you entered at the beginning
    tags = tags[linkNumber].get('href', None)
    print(tags)
    count = count - 1
    #switching the link you're gonna soup the next time loop runs
    myUrl = tags
