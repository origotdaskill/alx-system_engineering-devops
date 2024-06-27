#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
        else:
            print(f"HTTP error occurred: {http_err}")
        return 0
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
        return 0

# Example usage:


if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    subscribers = number_of_subscribers(subreddit)
    print(f"Subreddit '{subreddit}' has {subscribers} subscribers.")
