#!/bin/bash
# takes in a URL, sends request to that URL, print status
curl -sI -o /dev/null -w'%{http_code}' "$1"
