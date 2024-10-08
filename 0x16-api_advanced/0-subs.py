#!/usr/bin/python3
"""Module for task 0"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers
    to the subreddit"""
    import requests

    sub_info = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json",
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    status = sub_info.status_code
    if status != 200:
        return 0
    else:
        return sub_info.json()['data']['subscribers']
