#!/bin/bash
# takes in a URL, sends request to that URL/catch_me, data in JSON
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
