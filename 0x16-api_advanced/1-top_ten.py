#!/usr/bin/python3
"""Module for task 1"""


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    import json
    import requests
    with open('file.json', 'r') as f:
        header = json.load(f)
    url = f"https://oauth.reddit.com/r/{subreddit}/hot?limit=8&offset=0"
    resss = requests.get(url=url,
                         headers=header, allow_redirects=False,)
    if resss.status_code != 200:
        print('none')
    else:
        post = resss.json()['data']['children']
        for item in post:
            print(item['data']['title'])
