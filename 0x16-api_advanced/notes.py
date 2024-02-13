#!/usr/bin/python3
"""notes for styuding reddit api"""
import requests, requests.auth


CLIENT_ID = '9aGjbyymIGyp0GAHCVVxYg'
SECURITY_KEY ='3feUvnL5SJMdDieOLzHrT3043iRseg'

client = requests.auth.HTTPBasicAuth(CLIENT_ID, SECURITY_KEY)


    
#!/usr/bin/python3
"""
0. How many subs? task solution module
"""
import requests


def number_of_subscribers(subreddit):
    """
    a function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0.
    """
    if (subreddit is None or type(subreddit) != str):
        return 0
    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    resp = requests.get(url, headers, allow_redirects=False)
    data = resp.json()
    print(data)

number_of_subscribers('Python')
