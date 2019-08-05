import feedparser
import json
from bs4 import BeautifulSoup


url = feedparser.parse('https://revistaautoesporte.globo.com/rss/ultimas/feed.xml')
url = url['entries']

feed = {
    'feed': []
}


def crawler():

    for i in range(0, len(url)):
        data = {
            'item': dict(title={}, link={}, description=[])}
        data['item']['title'] = url[i]['title']
        data['item']['link'] = url[i]['link']
        # ---comenta
        soup = BeautifulSoup(url[i]['summary'], 'html.parser')
        for tag in soup.find_all(True):
            if tag.name == 'img':
                data['item']['description'].append({
                    'type': 'image',
                    'content': tag.get('src')
                })

            if tag.name == 'a':
                data['item']['description'].append({
                    'type': 'link',
                    'content': tag.get('href')
                })

            if tag.name == 'p':
                data['item']['description'].append({
                    'type': 'text',
                    'content': tag.get_text()
                })

            else:
                continue
        feed['feed'].append(data)


crawler()
print(feed)
print(feed['feed'][0]['item']['link'])
print(feed['feed'][0]['item']['description'][0]['content'])

# vai criar um arquivo Json--------------------
file = open('infogobo_auto_sport.json', 'wb')
data_string = json.dumps(feed, indent=4)
file.write(data_string.encode('latin1'))
file.close()
