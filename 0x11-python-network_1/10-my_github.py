#!/usr/bin/python3
""" script thst fetches https://alx-intrannet.hbtn.io/status """
import requests
from sys import argv

if __name__ == "__main__":
    user_name = argv[1]
    token = argv[2]
    url = "https://api.github.com/user"

    with requests.get(
            url, auth=(user_name, token)) as response:
        print(response.json().get('id'))
