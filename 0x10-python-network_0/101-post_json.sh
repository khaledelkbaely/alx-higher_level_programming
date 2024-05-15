#!/bin/bash
# displays only the status code of the response
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
