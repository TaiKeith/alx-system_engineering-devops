#!/usr/bin/python3
"""
This module uses a recursive function that queries the Reddit API
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    This function recursively queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'after': after}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code != 200:
            return None

        data = response.json().get('data', {})
        children = data.get('children', [])
        after = data.get('after', None)

        for child in children:
            hot_list.append(child.get('data', {}).get('title', 'No Title'))

        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    except requests.RequestException:
        return None
