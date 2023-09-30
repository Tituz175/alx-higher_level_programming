#!/usr/bin/python3
# Python script that takes in a URL, sends a request to the URL
# and displays the value of the X-Request-Id variable found
# in the header of the response.
# You must use the packages urllib and sys
# You are not allow to import packages other than urllib and sys
# The value of this variable is different for each request
# You don’t need to check arguments passed to the script (number or type)
# You must use a with statement
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode("UTF-8")
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html)
