#!/usr/bin/python3
"""
This module queries the Reddit API
"""

import requests


def top_ten(subreddit):
    """
    This function queries the Reddit API and prints the titles of the first 10
    hot posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {'User-Agent': 'My User Agent 1.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            children = response.json().get('data', {}).get('children', [])

            for i in range(10):
                print(children[i].get('data').get('title'))
        else:
            print("None")
    except requests.RequestException:
        print("None")
