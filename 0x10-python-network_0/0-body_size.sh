#!/bin/bash
# takes in a URL, sends a request to that URL,
curl -sIw --4 "$1" | grep -i Content-Length | awk '{print $2}'