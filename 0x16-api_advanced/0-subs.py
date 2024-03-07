#!/usr/bin/python3
"""
function to query subscribers on a given Reddit subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """return the number of subscribers on a given Reddit subreddit"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, allow_redirects=False)
    if (response.status_code == 400):
        return 0
    result = response.json().get('data')
    return result.get('subscribers')
