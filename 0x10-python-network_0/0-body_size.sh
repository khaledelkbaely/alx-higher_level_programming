#!/bin/bash
# send a request to url and displays the size of the body of the response
curl -s "$1" | wc -c
