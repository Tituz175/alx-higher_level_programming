#!/bin/bash
# takes in a URL, sends POST request to that URL, data in JSON
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
