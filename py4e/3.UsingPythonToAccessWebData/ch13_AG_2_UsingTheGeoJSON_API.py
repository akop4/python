import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Service URL and API key
api_key = False
if not api_key:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

def main():
    locations = getListOfLocations()

    for location in locations:
        place_id = getPlaceIdForLocation(location)
        print('Place ID:', place_id, 'for location:', location)
    else:
        print('Fin')

def getListOfLocations():
    return[
        'South Federal University',
        'Hanoi University of Science and Technology'
    ]

def getPlaceIdForLocation(location):
    parms = {
        'address':location,
        'key':api_key
    }

    url_with_key = serviceurl + urllib.parse.urlencode(parms)
    uh = urllib.request.urlopen(url_with_key, context=ctx)
    data = uh.read().decode()
    
    try:
        js = json.loads(data)
    except:
        js = False

    if not js or 'status' not in js or js['status'] != 'OK':
        return '==== Failure To Retrieve ===='
    
    return js['results'][0]['place_id']
        
main()
