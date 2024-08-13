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

    # Send a GET request to the API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse JSON response to get number of subscribers
        data = response.json().get('data', {})
        sub_count = data.get('subscribers', 0)
        return sub_count
    else:
        return 0
