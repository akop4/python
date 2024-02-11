import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def getListOfUrls():
    return[
        'http://py4e-data.dr-chuck.net/comments_42.json',
        'http://py4e-data.dr-chuck.net/comments_1885541.json'
    ]

def main():
    urls = getListOfUrls()

    for url in urls:
        sum_from_url = makeSumFromJSON(url)
        print('Sum:', sum_from_url, 'from URL:', url)
    else:
        print('Fin')

def makeSumFromJSON(url):
    uh = urllib.request.urlopen(url, context=ctx)
    
    data = uh.read()
    json_data = json.loads(data)['comments']
    
    return sum([int(x.get('count', '0')) for x in json_data])
        
main()
