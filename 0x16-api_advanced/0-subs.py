#!/usr/bin/python3
"""
This module queries the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """
    This function queries the Reddit API and returns the number of subscribers
    for a given subreddit
    """
    # Reddit API endpoint for getting subreddit info
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Setting a custom User-Agent to avoid too mant requests error
    headers = {'User-Agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        sub_count = data.get('subscribers', 0)
        return sub_count
    else:
        return 0
