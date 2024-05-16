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
        commits = response.json()
        i = 0
        for commit in commits:
            if i == 10:
                break
            print("{}: {}".format(
                  commit.get('sha'), commit.get(
                      'commit').get('author').get('name')))
            i += 1
