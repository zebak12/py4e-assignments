import urllib.request, urllib.parse
import json

service_url = 'http://py4e-data.dr-chuck.net/json?'
address = input('Enter location: ')
if len(address) < 1: address = 'South Federal University'

params = {}
params['key'] = 42
params['address'] = address
url = service_url + urllib.parse.urlencode(params)
print('Retrieving:', url)

url_handle = urllib.request.urlopen(url)
data = url_handle.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
# print(json.dumps(info, indent=4))

results = info['results'][0]
print('Place id:', results['place_id'])
