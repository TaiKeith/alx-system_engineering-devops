#!/usr/bin/python3
"""
This module uses a recursive function that queries the Reddit API and count
keywords in hot articles
"""

import requests
from collections import defaultdict


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    This function recursively queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'My User Agent 1.0'}
    params = {'after': after}
    
    if not hot_list:
        word_count = defaultdict(int)
    else:
        word_count = hot_list

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        if response.status_code != 200:
            return
        
        data = response.json().get('data', {})
        children = data.get('children', [])
        after = data.get('after', None)

        for child in children:
            title = child.get('data', {}).get('title', '').lower()
            words = title.split()

            for word in word_list:
                word_lower = word.lower()
                word_count[word_lower] += words.count(word_lower)

        if after:
            return count_words(subreddit, word_list, word_count, after)
        else:
            if word_count:
                sorted_words = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
                for word, count in sorted_words:
                    if count > 0:
                        print(f"{word}: {count}")
            return

    except requests.RequestException:
        return
