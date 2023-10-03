#!/usr/bin/python3
"""
uses the GitHub login details username and password, and the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <personal_access_token>")
        sys.exit(1)

    # the GitHub user API endpoint
    api_url = 'https://api.github.com/user'

    # Basic Authentication
    auth = (sys.argv[1], sys.argv[2])

    response = requests.get(api_url, auth=auth)

    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print(None)
