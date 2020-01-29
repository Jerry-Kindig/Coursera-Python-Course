import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)
mid = uh.read()
data = mid.decode()
print('Retrieved', len(mid), 'characters')

try:
    js = json.loads(data)
except:
    js = None

x = 0
y = 0

if js:
    lis = js['comments']
    for item in lis:
        x += 1
        y += int(item['count'])

print('Count:', x)
print('Sum:', y)