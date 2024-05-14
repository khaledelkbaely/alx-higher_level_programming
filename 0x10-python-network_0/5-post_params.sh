#!/bin/bash
# send a request to url and displays the size of the body of the response
curl -d 'email=test@gmail.com&subject=I will always be here for PLD' -s "$1"
