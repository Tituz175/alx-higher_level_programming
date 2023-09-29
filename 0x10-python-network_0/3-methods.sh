#!/bin/bash
# takes in a URL, sends OPTION request to that URL,
curl -sI -X OPTIONS "$1"
