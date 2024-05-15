#!/usr/bin/python3
""" script thst fetches https://alx-intrannet.hbtn.io/status """
from urllib.request import urlopen
from sys import argv

if __name__ == "__main__":
    url = argv[1]

    with urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))
