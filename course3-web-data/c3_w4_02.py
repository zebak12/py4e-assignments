from bs4 import BeautifulSoup
import urllib.request


def main():
    url = input('Enter URL: ')
    # url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
    count = int(input('Enter count: '))
    position = int(input('Enter position: '))
    print('Retrieving: ', url)

    for _ in range(count):
        soup = get_site_soup(url)
        href_tags = soup('a')
        url = href_tags[position-1].get('href', None)
        print('Retrieving: ', url)

def get_site_soup(url):
    html = urllib.request.urlopen(url).read()
    return BeautifulSoup(html, 'html.parser')


if __name__ == '__main__':
    main()
