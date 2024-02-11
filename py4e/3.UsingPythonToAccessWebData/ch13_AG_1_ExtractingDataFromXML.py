import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def getListOfUrls():
    return[
        'http://py4e-data.dr-chuck.net/comments_42.xml',
        'http://py4e-data.dr-chuck.net/comments_1885540.xml'
    ]

def main():
    urls = getListOfUrls()

    for url in urls:
        sum_from_url = makeSumFromXML(url)
        print('Sum:', sum_from_url, 'from URL:', url)

def makeSumFromXML(url):
    uh = urllib.request.urlopen(url, context=ctx)
    
    data = uh.read()
    tree = ET.fromstring(data)
    
    results = tree.findall('.//count')

    return sum([int(x.text) for x in results])
        
main()


