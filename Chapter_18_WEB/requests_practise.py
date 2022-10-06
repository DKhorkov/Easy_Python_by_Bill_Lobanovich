import requests


def get_music():
    url = 'https://itunes.apple.com/search'
    params = {'term': 'relax', 'media': 'music', 'entity': 'song', 'limit': 5}
    resp = requests.get(url, params=params)
    print(resp.status_code)
    return resp.json()


music = get_music()
print(music['resultCount'])
for result in music['results']:
    print(result)
