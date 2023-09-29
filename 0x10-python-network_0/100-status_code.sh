#!/bin/bash
# takes in a URL, sends request to that URL, print status
curl -sw'%{http_code}' "$1"
