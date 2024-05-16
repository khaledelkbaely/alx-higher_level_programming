#!/usr/bin/python3
""" script thst fetches https://alx-intrannet.hbtn.io/status """
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with requests.get(url) as response:
        body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
