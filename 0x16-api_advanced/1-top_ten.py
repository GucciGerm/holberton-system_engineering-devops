#!/usr/bin/python3
"""
    Here we will print the first 10 hot titles that are
    post listed for a given subreddit

"""
import json
import requests


def top_ten(subreddit):
    """
        top_ten - This func will print the titles of top 10

        subreddit - This is the reddit api

        Return: If not valid print None, else print titles!

    """
    headers = {'Content-Type': 'application/json',
               'User-agent': 'GucciGerm'}

    api_url = requests.get('https://api.reddit.com/r/{}/hot'.format(
        subreddit), headers=headers).json()

    try:
        for title in range(10):
            print(api_url['data']['children'][title]['data']['title'])
    except Exception:
        print(None)
