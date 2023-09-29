#!/bin/bash
# takes in a URL, sends OPTION request to that URL,
curl -sI -X GET "$1"/X-School-User-Id=98
