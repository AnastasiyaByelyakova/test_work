import requests

class APIHandler:
    def __init__(self, url='https://api.gbif.org/v1/literature/search'):
        self.url = url

    def run(self, limit):

        params = {'limit': limit}
        r = requests.get(self.url, params=params)

        if not r.json()['results']:
            print("No results found.")
            return

        results = []
        for n,i in enumerate(r.json()['results']):
            item = {
                'authors': [k['firstName']+' '+k['lastName'] for k in i['authors']],
                'keywords': i['keywords'],
                'title': i['title'],
                'abstract': i['abstract'],
                'topics': i['topics'],
                'published': i['published']
            }
            results.append(item)
            print(n,item['title'])

        return results

if __name__ == '__main__':
    handler = APIHandler()
    handler.run(8)
