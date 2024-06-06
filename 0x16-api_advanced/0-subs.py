#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print("OK")
        return 0
    results = response.json().get("data")
    print("OK")
    return results.get("subscribers")


if __name__ == "__main__":
    import sys
    subreddit = sys.argv[1] if len(sys.argv) > 1 else ""
    number_of_subscribers(subreddit)
