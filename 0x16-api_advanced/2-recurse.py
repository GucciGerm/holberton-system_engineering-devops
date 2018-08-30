#!/usr/bin/python3
"""
    Here we will use a recursive function to query the Reddit API

"""
import json
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
        recurse - This func will get a list of titles of all the hot articles
        for a given subreddit

        Return: If not valid return None, else return list of titles

    """
    headers = {'Content-Type': 'application/json',
               'User-agent': 'GucciGerm'}

    api_url = requests.get('https://api.reddit.com/r/{}/hot.json?after={}'
                           .format(subreddit, after), headers=headers).json()
    try:
        if subreddit is None:
            return (None)
        api_url = api_url.get('data')
        after = api_url.get('after')
        api_url = api_url.get('children')

        for idx in api_url:
            hot_list.append(idx['data'].get('title'))

        if after is None:
            return (hot_list)
        else:
            return recurse(subreddit, hot_list, after)
    except Exception:
        return (None)
