#!/bin/bash
# takes in a URL, sends POST request to that URL, data in JSON
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
