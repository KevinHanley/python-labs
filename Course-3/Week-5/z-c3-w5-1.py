import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


userurl = input('Enter a url: ')
fhand = urllib.request.urlopen(userurl)

data = fhand.read() #converts all xml to a string?
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

counts = tree.findall('.//comment') #find all the outer comment tags

increment = 0
for item in counts :
    increment = increment + int(item.find('count').text) #loop through inner count tags

print("Sum total is:", increment)
