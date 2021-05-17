#!/usr/bin/python3
"""
    Function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for
    a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
        Return that prints the title of the first 10 hot posts.
    """
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json?limit=10'
    headers = {
        'User-Agent': 'Chrome/90.0.4430.212 Safari/537.36'}
    req = requests.get(url, headers=headers, allow_redirects=False)
    if req.status_code != 200:
        print(None)
    else:
        list_titles = req.json().get('data').get('children')
        for title in list_titles:
            print(title.get('data').get('title'))
