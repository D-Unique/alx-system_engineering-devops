#!/usr/bin/python3
"""Module for task 1"""


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    import json
    import requests
    #with open('file.json', 'r') as f:
        #header = json.load(f)
    url = f"https://reddit.com/r/{subreddit}/hot.json"
    resss = requests.get(url=url,
                         headers={"User-Agent": "My-User-Agent"}, allow_redirects=False,)
    if resss.status_code != 200:
        print('none')
    else:
        post = resss.json()['data']['children']
        for item in post:
            print(item['data']['title'])
