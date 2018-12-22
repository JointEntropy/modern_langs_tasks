import lxml
from lxml import html
import requests
import re

regexp = r'<img[^>]+src="([^">]+)"'
def page_images(url):
    page = requests.get(url)

    # regulars
    # for s in re.findall(regexp, str(page.content)):
    #     yield s
    #lxml etree
    root = html.fromstring(page.content)
    for e in root.xpath('//img'):
       yield e.get('src')

if __name__ == '__main__':
    url = 'http://www.5zvezd.ru/'
    print(list(page_images(url)))
