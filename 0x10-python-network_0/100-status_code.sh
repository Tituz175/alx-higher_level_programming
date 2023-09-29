#!/bin/bash
# takes in a URL, sends request to that URL, print status
curl -sI -w'%{http_code}\n' "$1"
