#!/usr/bin/python3
# Python script that takes in a URL and an email,
# sends a POST request to the passed URL with the email as a parameter,
# and displays the body of the response (decoded in utf-8)
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        try:
            html = response.read().decode('utf-8')
            print(html)
        except urllib.error.HTTPError as e:
            print(e)
