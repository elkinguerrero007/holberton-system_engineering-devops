#!/usr/bin/python3
"""
0-subs
"""
import requests

api_url = "https://www.reddit.com"

default_header = {
    "Content-Type": "application/json",
    "User-agent": "Mozilla/5.0"
}


def top_ten(subreddit):
    """
    perform http request to reddit API to get number of
    subscribers by subreddit
    """
    url = api_url + "/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=default_header,
                            allow_redirects=False)

    if response.status_code >= 300:
        print("None")
        return 0

    children = response.json()["data"]["children"]

    for child in children:
        print(child['data']['title'])
