#!/usr/bin/python3
"subscribers count"

import requests

def number_of_subscribers(subreddit):
    headers = {
        'User-Agent': 'My User Agent 1.0',
    }
    params = {
        'format': 'json',
    }
    response = requests.get('https://oauth.reddit.com/r/' + subreddit + '/about', headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
