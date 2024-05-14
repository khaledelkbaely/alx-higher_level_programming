#!/bin/bash
# send a request to url and displays the size of the body of the response
curl --header 'X-School-User-Id: 98' -s "$1"
