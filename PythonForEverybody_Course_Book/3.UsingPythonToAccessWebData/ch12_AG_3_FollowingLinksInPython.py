from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

def main():
    urls = getListOfTuplesForParse()

    for (url, position, count) in urls:
        result = parseURL(url, position-1, count)
        print(result)
    
    print('Fin')

def getListOfTuplesForParse():
    # (URL, position, count)
    return [
        ('http://py4e-data.dr-chuck.net/known_by_Fikret.html', 3, 4),
        ('http://py4e-data.dr-chuck.net/known_by_Kalyana.html', 18, 7)
    ]

def parseURL(url, position, count):
    if not count > 0:
        return url
    
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    
    tags = soup('a')
    
    next_url = tags[position].get('href', None)
    if next_url:
        url = parseURL(next_url, position, count-1)
    
    return url
    
main()