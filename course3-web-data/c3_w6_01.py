import urllib.request, urllib.parse
import json

url = input('Enter location: ')
# url = 'http://py4e-data.dr-chuck.net/comments_42.json'
url_handle = urllib.request.urlopen(url)
print('Retrieving', url)

data = url_handle.read()
print('Retrieved', len(data), 'characters.')

info = json.loads(data)
comments = info['comments']

count = 0
count_sum = 0
for element in comments:
    count += 1
    count_sum += int(element.get('count', 0))

print('Count:', count)
print('Sum:', count_sum)
