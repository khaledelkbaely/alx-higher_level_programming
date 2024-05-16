#!/usr/bin/python3
""" script thst fetches https://alx-intrannet.hbtn.io/status """
from urllib.request import urlopen

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urlopen(url) as response:
        body = response.read()
        print("Body responce:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
