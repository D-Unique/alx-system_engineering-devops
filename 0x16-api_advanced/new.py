#!/urs/bin/python3

import requests
resss =requests.get('https://oauth.reddit.com/api/v1/me', headers={'user-agent': 'my-user-agent'}) 

print(resss.json())
