#!/usr/bin/python3
"""
    Function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for
    a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
        Return that prints the title of the first 10 hot posts.
    """
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    url = url + '?limit=100&?after=' + after
    headers = {
        'User-Agent': 'Chrome/90.0.4430.212 Safari/537.36'}
    req = requests.get(url, headers=headers, allow_redirects=False)
    if req.status_code != 200:
        return None

    list_titles = req.json().get('data').get('children')
    for title in list_titles:
        hot_list.append(title.get('data').get('title'))
    
    after = req.json().get('data').get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
        
