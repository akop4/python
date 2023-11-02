from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

def main():
    urls = getListURLsForParse()

    for url in urls:
        sum = parseURLForSum(url)
        print(sum)


def getListURLsForParse():
    return [
        'http://py4e-data.dr-chuck.net/comments_42.html',
        'http://py4e-data.dr-chuck.net/comments_1885538.html'
    ]

def parseURLForSum(url):
    # Ignore certificate
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    # Open and parse URL
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    # Get numbers from span
    tags = soup('span')
    sum = 0
    for tag in tags:
        sum += int(tag.contents[0])

    return sum

main()