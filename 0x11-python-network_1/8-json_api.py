#!/usr/bin/python3
""" script thst fetches https://alx-intrannet.hbtn.io/status """
import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = argv[1] if len(argv) > 1 else ""

    with requests.post(url, data={"q": letter}) as response:
        try:
            json_response = response.json()
            if json_response:
                print("[{}] {}".format(
                      json_response.get('id'), json_response.get('name')))
            else:
                print("No result")
        except Exception:
            print("Not a valid JSON")
