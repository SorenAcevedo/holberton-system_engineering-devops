#!/usr/bin/python3
""" This module use Reddit Api """
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
        Function that queries the Reddit API and returns
        a list containing the titles of all hot articles
        for a given subreddit.
    """
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'

    headers = {
        'User-Agent': 'Chrome/90.0.4430.212 Safari/537.36'}

    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    req = requests.get(url, headers=headers,
                       params=params, allow_redirects=False)

    if req.status_code != 200:
        return None

    data = req.json().get("data")
    after = data.get("after")
    count += data.get("dist")
    childrens = data.get("children")
    hot_list.extend([child.get("data").get("title") for child in childrens])

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
