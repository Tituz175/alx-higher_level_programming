#!/bin/bash
# takes in a URL, sends GET request to that URL, with an Header variable
curl -sH "X-School-User-Id:98" "$1"
