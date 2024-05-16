#!/usr/bin/python3
""" script thst fetches https://alx-intrannet.hbtn.io/status """
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    with requests.get(url) as response:
        if response:
            print(response.text)
        else:
            print("Error code: {}".format(response.status_code))
