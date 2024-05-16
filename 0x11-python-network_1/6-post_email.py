#!/usr/bin/python3
""" script thst fetches https://alx-intrannet.hbtn.io/status """
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = argv[2]

    with requests.post(url, data={'email': email}) as response:
        print(response.text)
