import requests
from bs4 import BeautifulSoup as BS

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
           }
url = 'https://.....'

req = session.get(url, headers=headers)

if req.status_code == 200:
    bsObject = BS(req.content, 'html.parser')

data = bsObject.prettify()  # encode('utf8')

handle = open('page.html', 'w')
handle.write(str(data))
handle.close()
