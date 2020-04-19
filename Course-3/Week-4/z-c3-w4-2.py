import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Cailean.html'

for i in range(7) :
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    links = list()
    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        links.append(tag.get('href', None))

    url = links[17]
    print(url)
