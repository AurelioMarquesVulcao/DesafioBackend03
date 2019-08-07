import feedparser
import json
from bs4 import BeautifulSoup

# Search all html content off
url = feedparser.parse('https://revistaautoesporte.globo.com/rss/ultimas/feed.xml')
url = url['entries']

feed = {
    'feed': []
}


def crawler():
    # will fetch all the titles and links of the articles
    for i in range(0, len(url)):
        data = {
            'item': dict(title={}, link={}, description=[])}
        data['item']['title'] = url[i]['title']
        data['item']['link'] = url[i]['link']
        # Search content of materials
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
                    'content': (str(tag.get_text())).strip('\n\t\xa0')
                })

            else:
                continue
        feed['feed'].append(data)


crawler()

# create a json file
with open('infogobo_auto_sport.json', 'w') as f:
    json.dump(feed, fp=f, indent=4, ensure_ascii=False)
