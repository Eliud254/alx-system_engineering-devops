#!/usr/bin/python3
"""Function that  prints hot posts on the given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print all the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "faithokoth"
            }
    params = {
            "limit": 10
            }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
