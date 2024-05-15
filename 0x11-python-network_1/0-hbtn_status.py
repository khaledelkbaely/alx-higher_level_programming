#!/usr/bin/env python
""" script thst fetches https://alx-intrannet.hbtn.io/status """
from urllib.request import urlopen

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urlopen(url) as response:
        body = response.read()
        print("Body responce:")
        print("\t-", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode("utf-8"))
