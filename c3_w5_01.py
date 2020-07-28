from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import urllib.request

url = input('Enter location: ')
# url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
print('Fetching: ', url)
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

count = 0
count_sum = 0
comment_tags = soup('comment')

for comment_tag in comment_tags:
    tree = ET.fromstring(str(comment_tag))
    count_content = tree.find('count').text
    if count_content:
        count += 1
        count_sum += int(count_content)
    
print('Count: ', count)
print('Sum: ', count_sum)
