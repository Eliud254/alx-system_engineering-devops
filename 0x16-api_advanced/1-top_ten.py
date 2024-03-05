#!/usr/bin/python3

import requests


def top_ten(subreddit):
    """
    Prints the titles of the top 10 hottest posts on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "eliudobure"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for non-2xx status codes

        results = response.json().get("data")
        for post in results.get("children"):
            print(post.get("data").get("title"))

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

