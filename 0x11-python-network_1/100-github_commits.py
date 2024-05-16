#!/usr/bin/python3
""" script thst fetches https://alx-intrannet.hbtn.io/status """
import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(
        repo, owner)

    with requests.get(url) as response:
        recent_ten_commits = response.json()[:11]
        for commit in recent_ten_commits:
            print("{}: {}".format(
                  commit.get('sha'), commit.get(
                      'commit').get('author').get('name')))
