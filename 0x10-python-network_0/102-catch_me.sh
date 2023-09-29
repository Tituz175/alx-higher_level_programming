#!/bin/bash
# takes in a URL, sends request to that URL/catch_me, data in JSON
curl -sI $1/catch_me
