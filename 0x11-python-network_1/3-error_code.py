#!/usr/bin/python3
""" script thst fetches https://alx-intrannet.hbtn.io/status """
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    try:
        with urlopen(url) as response:
            body = response.read()
            body = body.decode('utf-8')
            print(body)
    except HTTPError as error:
        print("Error code: {}".format(error.status))
