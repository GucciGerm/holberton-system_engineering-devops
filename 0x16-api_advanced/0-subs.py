#!/usr/bin/python3
"""
   Here we will be getting the total amount of subscribers from a reddit API

"""
import json
import requests


def number_of_subscribers(subreddit):

    """
        number_subscribers - This function will querie the reddit API and
        will return the number of subscribers (not active, total users)

        subreddit: This is the Reddit API

        Return: If invalid return 0, else return the number of subscribers

    """

    headers = {'Content-Type': 'application/json',
               'User-Agent': 'GucciGerm'}

    api_url = requests.get('https://api.reddit.com/r/{}/about'.format
                           (subreddit), headers=headers)

    try:
        reddit_data = api_url.json().get('data')
        subs = reddit_data.get('subscribers')
        return (subs)
    except Exception:
        return (0)
