#!/bin/bash
# takes in a URL, sends POST request to that URL, data in JSON
curl -sX POST -d @"$2" "$1"
