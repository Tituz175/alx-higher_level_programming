#!/usr/bin/python3
"""
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""
import requests
import sys

if __name__ == "__main__":
    q = ""
    if sys.argv[2]:
        q = sys.argv[2]

    res = requests.post(f"{sys.argv[1]}?q={q}")
    print(res.text)
