import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True :
    address = input('Enter an Address URL: ')
    if len(address) < 1:
        break

    connection = urllib.request.urlopen(address, context=ctx)
    data = connection.read().decode() #UTF-8?

    try:
        js = json.loads(data)
    except:
        js = None

    comments = js['comments']
    sumtotal = 0
    for item in comments :
        sumtotal = sumtotal + int(item['count'])

    print('Total is:',sumtotal)
