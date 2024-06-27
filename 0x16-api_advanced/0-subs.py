#!/usr/bin/python3
"""
The module documentation
"""

import requests


def number_of_subscribers(subreddit):
    """query a subreddit and retrive no of subscribers"""

    headers = {"User-Agent": "Edson/1.0"}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return (0)
