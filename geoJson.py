import urllib.parse, urllib.error, urllib.request
import json
import ssl

api_key = False
serviceUrl = 'http://py4e-data.dr-chuck.net/json?'
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

if api_key is False:
    api_key = 42
    serviceUrl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceUrl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('What\'s the location? \n')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    #merging the json address with the location
    url = serviceUrl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    fhandle = urllib.request.urlopen(url)
    reading = fhandle.read().decode()
    print('Retrieved', len(reading), 'characters')

    try:
        js = json.loads(reading)
    except:
        js = None


    print('Place id', js['results'][0]['place_id'])
    break
