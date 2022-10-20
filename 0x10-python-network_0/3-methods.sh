#!/bin/bash
# display all HTTP methods the server will accept
curl -s "$1" -X OPTIONS
