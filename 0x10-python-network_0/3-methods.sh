#!/bin/bash
# takes in a URL, sends OPTION request to that URL,
curl -sXI OPTIONS "$1"
