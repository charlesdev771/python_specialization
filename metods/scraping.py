
#Important! pip3 install beautifulsoup4; pip3 install requests
import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'
resp = requests.post(url)

html = BeautifulSoup(resp.text, 'html.parser')

for quest in html.select('#question-summary-558072'):
    title = quest.select_one('.s-link')

    print(title.text)
