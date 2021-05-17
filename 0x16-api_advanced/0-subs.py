#!/usr/bin/python3
""" This module use Reddit Api """
import requests


def number_of_subscribers(subreddit):
    """ Function that queries the Reddit API
        return number of subscribers
        0 if an invalid subreddit is given
        """
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    headers = {
        'User-Agent': 'Chrome/90.0.4430.212 Safari/537.36'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    subs = response.json().get('data').get('subscribers')
    return subs
