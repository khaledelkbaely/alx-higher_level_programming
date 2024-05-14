#!/bin/bash
# send a request to url and displays the size of the body of the response
curl -is "$1" | grep "Allow" | cut -d ':' -f2-
