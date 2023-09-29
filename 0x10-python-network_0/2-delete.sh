#!/bin/bash
# takes in a URL, sends DELETE request to that URL,
curl -sX DELETE "$1"
