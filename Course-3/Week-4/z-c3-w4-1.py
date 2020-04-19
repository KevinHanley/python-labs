from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urlopen('http://py4e-data.dr-chuck.net/comments_448519.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
# Retrieve all of the span tags

tags = soup('span')
for tag in tags:
    tagvalue = int(tag.contents[0])
    count = count + tagvalue

print(count)
