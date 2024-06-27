#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        elif response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
            return 0
        else:
            print(f"Error: Status code {response.status_code}")
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return 0

# Example usage:


if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    subscribers = number_of_subscribers(subreddit)
    print(f"Subreddit '{subreddit}' has {subscribers} subscribers.")
