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
    if len(sys.argv) > 1:
        q = sys.argv[1]

    data = {"q": q}

    res = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        user_data = res.json()
        print(f"[{user_data.get('id')}] {user_data.get('name')}")
    except:
        print("No result")
