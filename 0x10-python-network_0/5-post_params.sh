#!/bin/bash
# takes in a URL, sends POST request to that URL,
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
