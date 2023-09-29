#!/bin/bash
# takes in a URL, sends request to that URL/catch_me, data in JSON
curl -sXL PUT -H "user_id=98" "0.0.0.0:5000/catch_me"
