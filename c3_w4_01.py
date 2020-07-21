from bs4 import BeautifulSoup
import urllib.request

url = input('Enter -')

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

count = 0
sum = 0

tags = soup('span')

for tag in tags:
  content = tag.contents[0]
  sum += int(content)
  count += 1
  
print('Count', count)
print('Sum', sum)