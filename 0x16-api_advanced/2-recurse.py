#!/usr/bin/python3
""" This module requests Reddit API """

import requests

api_url = "https://www.reddit.com"

header = {"Content-Type": "application/json",
          "User-Agent": "Mozilla/5.0"}


def hot(subreddit, after=None):
    """get hot subreddit"""
    url = api_url + "/r/{}/hot.json".format(subreddit)
    params = {"after": after}

    response = requests.get(url, headers=header, allow_redirects=False,
                            params=params)
    if response.status_code >= 400:
        return None
    try:
        return response.json()
    except Exception:
        return None


def recurse(subreddit, hot_list=None, after=None):
    """ Return the hot posts list. """
    if hot_list is None:
        hot_list = []

    response = hot(subreddit, after)
    if not response:
        return None
    data = response.get("data")
    children = data.get("children")
    hot_list += [child.get("data").get('title') for child in children]

    if not data.get('after'):
        return hot_list

    return recurse(subreddit, hot_list, data.get('after'))
