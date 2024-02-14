#!/usr/bin/python3
"""
requests about info from reddit api
"""
import requests


def top_ten(subreddit):
    """
    first 10 hot posts listed for a given subreddit.
    """

    headers = {
        "User-Agent": "0x16. API_advanced-e_kiminza"
    }
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)
