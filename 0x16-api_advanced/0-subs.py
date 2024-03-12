#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API for the subscriber count of a subreddit.

    Args:
        subreddit: The name of the subreddit to query

    Returns:
        The number of subscribers for the subreddit, or 0 if an error occurs
        or the subreddit is invalid.
    """

    url = f"https://reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "u/obureeliud"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        data = response.json()
        subscribers = data.get("data", {}).get("subscribers", 0)
        print("OK")
        return subscribers
    except requests.exceptions.RequestException as e:
        print(f"Error querying Reddit API: {e}")
        return 0
